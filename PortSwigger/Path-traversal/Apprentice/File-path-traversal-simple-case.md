# [File path traversal, simple case] — [PortSwigger] — [Apprentice]
**Date:** 2026-06-13
 
---
 
## Vulnerability / core concept
Path Traversal

## What made me stuck
This level was very easy.
 
## What unblocked me
`null`
 
---


## Attack path
1) During inspection of web application, we can see that when we are opening `/product?productId=x` endpoint, image gets requesting in separete request by its name.
2) All we need to do is to send that request to Replay in Caido or Repeater in Burp and change the name of image to something like `../../../../../etc/passwd`. This will retrieve `/etc/passwd` and solve the lab.

---


## Payload / key command
```html
GET /image?filename=../../../../../etc/passwd HTTP/1.1
...
```

---


## What I'd recognize faster next time
It is important to pay attention to resources that are getting requested by their filenames from folders withing system. If not protected properly, there is high chance of exploiting path traversal.
 

