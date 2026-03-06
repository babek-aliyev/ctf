# Challenge Name: User ID controlled by request parameter 
# Platform: PortSwigger
# Difficulty: Apprentice

## 1. Vulnerability Type
IDOR - Horizontal Privilege Escalation

## 2. Root Cause
Application does not verify that the requested user ID belongs to the authenticated user.
## 3. Attack Surface
`/my-account?id=wiener`

## 4. Exploit Method
Changing `?id=wiener` to `?id=carlos` exploits horizontal privilege escalation. After modifying parameter value it is possible to get unauthorized access to `carlos` user's API key.

## 5. Payload / Technique
`/my-account?id=carlos`

## 6. Impact
Unauthorized access to other users sensitive data such as API key, PII (personally identifiable information), etc. In real world application can lead to severe user data leak, financial loss, data theft.

## 7. Reusable Pattern
If application does not verify authorization of users using Session cookies and JWT tokens, it is possible to modify parameters like `id` and get access to existing user accounts, data, etc.

## 8. Key Takeaway
Always validate authentication and authorization server-side using at least session cookies and JWT tokens. Do not blindly trust user requests and its parameters without proper validation.
