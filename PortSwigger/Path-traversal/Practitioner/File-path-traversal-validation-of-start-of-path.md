# [File path traversal, validation of start of path] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-13
 
---
 
## Vulnerability / core concept
Path Traversal

## What made me stuck
This level was actually pretty easy.
 
## What unblocked me
`null`
 
---


## Attack path
1) During inspection we can notice that this web application send GET request with file path to retrieve the image of the product. 
2) We send this request to Replay in caido and start testing it. The first thing that came to my mind is just simple remove filename and replace it with `../../../../../../etc/passwd` to see what happens. To my surprise, I solved this lab from this very first attempt. However, I still tested other techniquest, during those tests i was getting `Missing parameter 'filename'`. I think this is because this web application checks whether the filename starts with specific base path `/var/www/images`. Therefore, after application sees that we our filename includes base path, it allows us to perform path traversal. This way we can access `/etc/passwd` and solve this lab.

---


## Payload / key command
```bash
GET /image?filename=/var/www/images/../../../../../../etc/passwd HTTP/1.1
...
```
Note: it is fine to use more `../` than we actually need. That way we can just ensure ourselves that we are in the root folder.

---


## What I'd recognize faster next time
If we notice some filename with specific base path like `/var/www/images` it is important to test this path using both with and without that path. Web application might have very insecure design that only checks whether filename includes that base path or not.
 

