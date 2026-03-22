# Challenge Name: Brute-forcing a stay-logged-in cookie 
# Platform: PortSwigger
# Difficulty: Practitioner

## 1. Vulnerability Type
Brute-Force

## 2. Root Cause
The application uses a `stay-logged-in` cookie that stores credentials in the format base64(username:md5(password)).
Because the cookie is not protected with a secure signature, an attacker can generate valid cookie values and brute-force passwords offline.
## 3. Attack Surface
`/my-account?id=`

## 4. Exploit Method
The attacker knows the victim's username and has a list of possible passwords.

Instead of brute-forcing the login endpoint, the attacker targets the `stay-logged-in` cookie, which contains base64(username:md5(password)).

Steps:
1. Hash each password using MD5
2. Prepend the username (e.g., carlos:)
3. Encode the result in Base64
4. Use the generated values to brute-force the stay-logged-in cookie

Because this endpoint does not enforce rate limiting, the attacker can test many values without being blocked.
## 5. Payload / Technique
```bash
┌──(kali㉿kali)-[~/Desktop]
└─$ ffuf -u https://0a7600c70497271880b2f80d00ab0092.web-security-academy.net/my-account?id=carlos \
-H "Cookie: session=8bESkJfcxqxwwqmu0xbFYX4QtTttVSYX; stay-logged-in=FUZZ" \
-w base64.txt
-ac
```

## 6. Impact
Improperly protected authentication cookies allow attackers to bypass login protections and perform brute-force attacks.
## 7. Reusable Pattern
When testing authentication mechanisms, verify whether persistent login cookies contain predictable or reversible values that can be brute-forced without rate limiting.
## 8. Key Takeaway
Authentication cookies must be securely signed and must not contain reversible credential data. Sensitive tokens should always be protected against brute-force attacks.

