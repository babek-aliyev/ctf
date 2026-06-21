# [Source code disclosure via backup files] — [PortSwigger] — [Apprentice]
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
1) First, we need to map our attack surfaces in this web application.
2) After deep inspection, we see that the only thing we can change and test is `productId` parameter in URL, which does not reveal anything.
3) Then, I also checked the HTML code to see if there are any comments that might be useful for us, but yet again, unfortunate.
4) The last thing that came to my mind is to check `robots.txt` and `sitemap.xml`. And it a right call! Checking `robots.txt` reveal a hidden path `/backup` that we did not know about before.
5) After we move to `/backup` path, we see a link that redirects us to source code. Now, all we need to do is to find database password and solve this lab.

---


## Payload / key command
```bash
yourlabnumber.web-security-academy.net/backup/ProductTemplate.java.bak
```
This path will reveal the source code where you can find database password.
---


## What I'd recognize faster next time
Checking `robots.txt` and `sitemap.xml` is as important as finding any other information disclosure vulnerabilities. There is a chance that we will find a path that we did not know about before: more information means more attack surface.



