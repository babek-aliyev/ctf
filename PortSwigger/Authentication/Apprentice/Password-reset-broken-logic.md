# Challenge Name: Password reset broken logic 
# Platform: PortSwigger
# Difficulty: Apprentice

## 1. Vulnerability Type
Broken Authentication – Password Reset Logic Flaw
## 2. Root Cause
Application does not validate the `temp-forgot-password-token` on the server side, allowing an attacker to reset the password of another user.
## 3. Attack Surface
`/forgot-password`

## 4. Exploit Method
Attacker requests a password reset for their own account and receives a reset link containing a temporary token. The attacker then intercepts the request and modifies the `username` parameter to another user's username. Because the server does not validate that the token belongs to the specified user, the attacker can reset the victim's password.
## 5. Payload / Technique
Request modification, changing `username` parameter to victim's username.

## 6. Impact
Account takeover of arbitrary users, leading to unauthorized access, potential data leakage, and loss of user control.
## 7. Reusable Pattern
When testing password reset functionality, always verify that reset tokens are validated server-side and bound to the correct user.

## 8. Key Takeaway
Security-sensitive tokens must always be verified server-side and must not rely on client-controlled parameters.

