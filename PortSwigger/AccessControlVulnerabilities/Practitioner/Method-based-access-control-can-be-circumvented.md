# Challenge Name: Method-based access control can be circumvented 
# Platform: PortSwigger
# Difficulty: Practitioner

## 1. Vulnerability Type
Broken Access Control - Vertical Privilege Escalation

## 2. Root Cause
Web application does not verify authorization and ownership server-side which leads to unauthorized access to admin panel and endpoints.

## 3. Attack Surface
`/admin-roles`

## 4. Exploit Method
Observing from `adminstrator:admin` account, we observer the following endpoints: `/admin` and `/admin-roles`. As authenticated user `wiener:peter` it is possible to modify request using Burp Suite and promote yourself to admin using the `GET` request.

## 5. Payload / Technique
/admin-roles?username=wiener&action=upgrade

## 6. Impact
Users can get unauthorized access to admin panel and admin actions that can lead to data loss and data leak. In this case, it also leads to vertical privilege escalation.
## 7. Reusable Pattern
Check endpoints such as admin panel and admin actions (or other endpoints that require authorization) to see if they are exploitable.

## 8. Key Takeaway
Always validate authorization and ownership server-side to prevent unauthorized access from users. 


