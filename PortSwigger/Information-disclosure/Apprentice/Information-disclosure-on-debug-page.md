# [Information disclosure on debug page] — [PortSwigger] — [Apprentice]
**Date:** 2026-06-21
 
---
 
## Vulnerability / core concept
Information Disclosure

## What made me stuck
This level was very easy.

## What unblocked me
`null`
 
---


## Attack path
1) First, we need to analyze the whole web application to map our attack surface.
2) After inspection, we see that the only thing that we can test by changing is parameters in URL. I tried to `productId` invalid, however, the application did not respond with anything useful.
3) Then, I decided to use developers tools, specifically inspection to see if there is something worth seeing. And there was! There was a debug link, that contained all technical information about this web application.
4) Now, all we need to do is to find `SECRET_KEY` and solve this lab.

---


## Payload / key command
```bash
yourlabnumber.web-security-academy.net/cgi-bin/phpinfo.php
```
Visit this debug page and find `SECRET_KEY`.

---


## What I'd recognize faster next time
Sometimes, it is possible that developers mistakenly leave sensitive information in the HTML comments that might expose the technical information about the web application.



