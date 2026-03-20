# Challenge Name: Username enumeration via account lock 
# Platform: PortSwigger
# Difficulty: Practitioner

## 1. Vulnerability Type
Username Enumeration

## 2. Root Cause
The application locks accounts after multiple failed login attempts, but returns different error messages for existing and non-existing usernames, allowing attackers to identify valid accounts.
## 3. Attack Surface
`/login`

## 4. Exploit Method
The attacker is provided with a list of usernames.

To trigger account lockout, each username is repeated multiple times in the wordlist so that several failed attempts are sent for each account.

When fuzzing the login endpoint, existing usernames eventually return an account lock message, while non-existing usernames continue to return a generic login error.

This difference allows the attacker to identify valid usernames.

After identifying a valid username, the attacker performs password brute-force to gain access to the account.
## 5. Payload / Technique
The username list was modified to repeat each entry multiple times in order to trigger the account lock mechanism during fuzzing. First we identify valid username and then brute-force:
```bash
┌──(kali㉿kali)-[~/Desktop]
└─$ ffuf -u https://0a53006503dc994d816b0741008b00e4.web-security-academy.net/login \
-w usernames.txt \
-X POST -d "username=FUZZ&password=dummypass" \
-ac
```
```bash
┌──(kali㉿kali)-[~/Desktop]
└─$ ffuf -u https://0a53006503dc994d816b0741008b00e4.web-security-academy.net/login \
-w passwords.txt \
-X POST -d "username=agent&password=FUZZ" \
> -ac
```

## 6. Impact
Different error messages for valid usernames can make brute-forcing account much easier and faster for attacker.

## 7. Reusable Pattern
Determine if application uses account block: if it does use, determine if you get different error messages for many tries or not.

## 8. Key Takeaway
Always return consistent errors, response time, length, number of words in response to prevent username enumeration that can lead to brute-forcing.


