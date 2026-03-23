# Challenge Name: Password brute-force via password change 
# Platform: PortSwigger
# Difficulty: Practitioner

## 1. Vulnerability Type
Broken Access Control / Password Brute-Force via Logic Flaw
## 2. Root Cause
The application allows password change requests without properly verifying that the request belongs to the authenticated user.
Additionally, the application returns different responses depending on whether the current password is correct and whether the new passwords match.
These differences allow an attacker to brute-force the victim's password.

## 3. Attack Surface
`/my-account/change-password`

## 4. Exploit Method
The password change function accepts a username parameter and does not verify that the username belongs to the logged-in user.

The response behavior differs in several cases:

1. Current password incorrect + new passwords different → "Current password is incorrect"
2. Current password incorrect + new passwords match → Redirect to login page
3. Current password correct + new passwords different → "New passwords do not match"
4. Current password correct + new passwords match → Password changed (200 OK)

Because of these differences, the attacker can brute-force the victim's current password by sending requests with the victim's username and checking the response.

After finding the correct password, the attacker can change the victim's password and gain full access to the account.
## 5. Payload / Technique
```bash
┌──(kali㉿kali)-[~/Desktop]
└─$ ffuf -u https://0a74005703ba1a4f816a0c6300c70084.web-security-academy.net/my-account/change-password \
> -w passwords.txt \
> -X POST -d "username=carlos&current-password=FUZZ&new-password-1=peter&new-password-2=xurrami" \
> -mr "New" \
> -H "Cookie: session=zRi6CjxJEVcf6xPL9vVyTJ8Oj8ys6ZLF; session=8XazVLhLo3YKloAcfManMA98SMK4l2eA" \
> -ac
```

## 6. Impact
An attacker can brute-force the victim's password and change it without authorization, leading to full account takeover.

## 7. Reusable Pattern
Check password change functionality for:
- missing authorization checks
- username parameter manipulation
- different error messages
- different response codes
- different redirects

These differences may allow password brute-force or account takeover.
## 8. Key Takeaway
Password change endpoints must:
- verify user identity server-side
- ignore user-controlled username parameters
- return consistent responses
- implement rate limiting

