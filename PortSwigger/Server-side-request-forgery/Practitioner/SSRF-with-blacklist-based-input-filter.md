# [SSRF with blacklist-based input filter] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-12
 
---
 
## Vulnerability / core concept
Server-side Request Forgery

## What made me stuck
Nothing, this level was pretty straightforward, so solved it pretty quickly.
 
## What unblocked me
`null`
 
---


## Attack path
1) We can notice that web application sends request to its internal server to retrieve the amount of products.
2) I immediately tried to send request to `http://stock.weliketoshop.net/admin`, however, it did not work and i got error that claimed internal server is protected.
3) After thinking, i decided to play around with this request in Repeater. Some tries later, i noticed that `AdMiN` worked! It gave me a different errorsaying missing parameter. I decided to replace `stock.weliketoshop.net` with `localhost` and got error message related to internal server protection again.
4) Similar with admin, i wrote `LocalHost` and it bypassed it again! Now i got another error saying `Could not connect to external stock check service`.5) I thought this might be because of port, what if it is on another port, so i decided to remote port completely. I got response 200! It worked.
6) I noticed an endpoint saying `/admin/delete?username=carlos`. I send request to it (with modified admin of course) and i deleted user carlos and solved the lab.

---


## Payload / key command
```bash
POST /product/stock HTTP/1.1
...


stockApi=http://localHost/admiN/delete?username=carlos
```


---


## What I'd recognize faster next time
Using blacklist-based security measurements is not best idea to protect application from external attacks. There is almost always a way to bypass these blacklist-based protections: its obfuscating the payload, encoding, or something else.
 

