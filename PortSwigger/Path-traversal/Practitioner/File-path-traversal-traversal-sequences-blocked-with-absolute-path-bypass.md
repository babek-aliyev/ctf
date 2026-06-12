# [File path traversal, traversal sequences blocked with absolute path bypass] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-13
 
---
 
## Vulnerability / core concept
Path Traversal

## What made me stuck
This leves was really easy and I solved it very quickly.
 
## What unblocked me
`null`
 
---


## Attack path
1) During inspection we can notice that web application send GET request to fetch image on `/product?productId=x` endpoint to get image of the product. It does it by searching for filename in system directory.
2) This web app does not allow us to use path traversal, however, if we just use `/etc/passwd` it will work and solve the lab. This is because web app allows relative path traversal, where we can simply search for root folder using `/` as a first character.

---


## Payload / key command
```bash
GET /image?filename=/etc/passwd HTTP/1.1
...
```

---


## What I'd recognize faster next time
It is important to check both absolute path bypass and relative path bypass together. If one does not work, there is a chance that application does not block the other.
 

