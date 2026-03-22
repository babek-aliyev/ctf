# Challenge Name: 2FA broken logic
# Platform: PortSwigger
# Difficulty: Practitioner

## 1. Vulnerability Type
Broken 2FA Logic

## 2. Root Cause
Web application sends 2FA code based only on cookie value `verify` without nverifying account password. After sending 2FA code using cookie, web application does not use rate limit or account block, that makes it possible to brute-force 2FA code.

## 3. Attack Surface
`/login2`

## 4. Exploit Method
Attacker uses his own authenticated credentials to move to 2FA login page. Upon sending request, attacker changes `verify` in cookie from his username to victim's username. This will send 2FA code to victim's email address. Because application does not use rate limit or account block, using tool like `ffuf` attacker can brute-force 4-digit 2FA code and gain access to victim's account.

## 5. Payload / Technique
```bash
┌──(kali㉿kali)-[~/Desktop]
└─$ ffuf -u https://0a5a003304da103084124fa100ee0028.web-security-academy.net/login2 \
-H "Cookie: session=6ADQ9VqxRwsFlp5mSC5aIPsFYpBehqAQ; verify=carlos" \
-X POST -d "mfa-code=FUZZ" \
-w codes.txt \
-t 64 \
-ac
```

## 6. Impact
Just by knowing the username of victim, attacker can gain unauthorized access to victim's account.

## 7. Reusable Pattern
If application solely relies on cookie value to send 2FA code and does not have rate limit or account block restirictions, it is possible to brute-force the 2FA code.

## 8. Key Takeaway
Always have rate limit or account block or combination of both of them to prevent brute-forcing. Additionally, never rely solely on cookie value to send or request date from user.


