# [Information disclosure in error messages] — [PortSwigger] — [Apprentice]
**Date:** 2026-06-21
 
---
 
## Vulnerability / core concept
Information Disclosure

## What made me stuck
This level was very easy to solve.

## What unblocked me
`null`
 
---


## Attack path
1) First, we need to check all functionality that this web application has so we can map the attack surfaces.
2) After inspection, we see that there is almost nothing to test, except one thing. It is the `productId` parameter in URl.
3) I changed it from number to a character like `a`, and it revealed a big error, which revealed the framework version. Now, all we need to do is submit this version and solve the lab.

---


## Payload / key command
```bash
yourlabnumber.web-security-academy.net/product?productId=a
```
---


## What I'd recognize faster next time
It is important to check and map your attack surface and try to get as much as information you can. The explicit errors are our biggest friends as they reveal the underneath technical details that might come in handy.



