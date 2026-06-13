# [File path traversal, traversal sequences stripped with superfluous URL-decode] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-13
 
---
 
## Vulnerability / core concept
Path Traversal

## What made me stuck
This lab was pretty easy and straightforward, I solved it very quickly.
 
## What unblocked me
`null`
 
---


## Attack path
1) During inspection of web application using web proxies, we can notice that web app retrieves image of the product using GET request with filename. This file is retrieved from system directory which means there is a potential of path traversal.
2) After some testing, we can see that web application successfully filters both `../` and its url-encoded version `%2E%2E%2F`. However, this web application has an unintented behavior to decode the url twice. That means if we encode our url-encoded payload again, this application will decode it into normal url-encode that will be accepted. This way we bypass path traversal block, access `/etc/passwd` and solve the lab.

---


## Payload / key command
Our payload is double encoded here:
```bash
 ../        →  (URL encode)  →  %2E%2E%2F
  %2E%2E%2F  →  (URL encode)  →  %252E%252E%252F
```
and our request looks like this:
```bash
GET /image?filename=..%252F..%252F..%252F..%252F..%252Fetc%252Fpasswd HTTP/1.1
...
```

---


## What I'd recognize faster next time
It is important to check all types of encodings to make sure we did a good throughout pentest of path traversal. As in this lab, our target may have decode our payload in a such way that it will make it bypass web app's security filters and be exploited.
 

