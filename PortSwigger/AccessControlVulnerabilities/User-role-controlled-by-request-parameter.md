# Challenge Name: User role controlled by request parameter
# Platform: PortSwigger
# Difficulty: Apprentice

## 1. Vulnerability Type
Broken Access Control – Privilege escalation via client-controlled role parameter.
## 2. Root Cause
The application determines authorization based on client-side cookie:
```bash
Admin=false
```
The server trusts client-side request and grants admin privilege if:
```bash
Admin=false  ->  Admin=true
```
By modifying cookie client can get privilege escalation.
## 3. Attack Surface
`/admin`

## 4. Exploit Method
1) Navigate to `/admin` endpoint
2) Intercept and change `Admin` value to be `true` inside `Cookie` header.
3) Do this to every request
4) Delete user `carlos` using admin privilege

## 5. Payload / Technique
`Admin=true`

## 6. Impact
Unauthorized access to `/admin` endpoint. Vulnerable admin panel that can lead to data loss and full administrative control by hackers.

## 7. Reusable Pattern
Intercept all admin privileged requests and modify their `Admin` value to be `true` to gain unauthorized access to admin functionalities.

## 8. Key Takeaway
Always validate roles server-side. Do not trust authorization to `Cookie` header as it can be easily modified by proxy tools like Burp Suite, OWASP Zap, etc.


