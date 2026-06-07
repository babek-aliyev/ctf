# Authentication Bypass via Encryption Oracle — PortSwigger — Practitioner

**Date:** 2026-06-08

---

## Vulnerability / Core Concept

Authentication Bypass via Encryption Oracle

---

## What Made Me Stuck

This lab was challenging because it introduced several concepts I wasn't fully familiar with, so I had to do significant research and carefully study the write-up before I could understand the solution.

---

## What Unblocked Me

After reading the write-up and researching the unfamiliar areas, I fully understood the attack and was able to replicate the solution independently.

---

## Attack Path

1. When logging into the account, there is an option to stay signed in.

2. When this option is selected, the application generates an encrypted cookie to maintain the session — instead of relying solely on a standard session cookie, this encrypted value is used to verify identity.

3. After inspecting the web application further, a strange behavior appears in the comment section under posts. When an invalid email is submitted, the input gets encrypted, and then the application decrypts it back and displays it in an error message:
   ```
   Invalid email address: <our-input>
   ```
   This means the application is both encrypting and decrypting user-controlled input and revealing the result — a classic **encryption oracle**.

4. By copying the stay-signed-in cookie value into the notification cookie and sending a `GET` request, the application decrypts it and reveals the plaintext format: `username:timestamp` (e.g. `wiener:1749384000`). This tells us exactly what the administrator's cookie needs to contain.

5. The goal is now to encrypt `administrator:<timestamp>` and use it as a forged stay-signed-in cookie. However, there is a complication.

6. The comment endpoint always prepends `Invalid email address: ` (23 characters) to our input before encrypting it. This prefix will be included in the ciphertext, so we cannot directly produce a clean encryption of `administrator:<timestamp>`.

7. To work around this, we exploit the fact that the encryption uses **block ciphers** — each block is 16 bytes. If we can make the unwanted prefix occupy an exact number of complete blocks, we can simply discard those blocks from the ciphertext without affecting the rest.

8. The steps to achieve this are:

   - `Invalid email address: ` is 23 characters. To round this up to 32 (two complete 16-byte blocks), we need to add **9 padding characters** before our payload:
     ```
     bbbbbbbbbadministrator:<timestamp>
     ```
   - Submit this as the email input via `POST /post/comment` to get the encrypted value back.
   - URL-decode → Base64-decode → convert to hex.
   - Delete the **first 32 hex-encoded bytes (64 hex characters)** from the hex string. This removes the two blocks containing `Invalid email address: bbbbbbbbb`, leaving only the encrypted `administrator:<timestamp>`.
   - Convert the remaining hex back: hex-decode → Base64-encode → URL-encode.

9. Finally, open the application, delete the session cookie, set the stay-signed-in cookie to this crafted value, and refresh the page. The application will decrypt it, recognize `administrator:<timestamp>` as a valid identity, and log you in as the administrator. From there, delete user Carlos to complete the lab.

---

## Payload / Key Commands

| Purpose | Endpoint |
|---|---|
| **Encrypt input** | `POST /post/comment` — submit crafted email to trigger encryption |
| **Decrypt input** | `GET /post?postId=x` — triggers the error message that reveals decrypted value |

---

## What I'd Recognize Faster Next Time

If an application both encrypts and decrypts user-controlled input and reveals the result, this is an encryption oracle. Combined with block cipher structure, it may allow an attacker to forge encrypted tokens and bypass authentication entirely.
