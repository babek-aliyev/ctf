# [File path traversal, traversal sequences stripped non-recursively] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-13
 
---
 
## Vulnerability / core concept
Path Traversal

## What made me stuck
The technique that is used in this lab was new to me, so I had to do some research before doing this lab.
 
## What unblocked me
After doing some research in owasp and using ai, I found the right technique to exploit this lab.
 
---


## Attack path
1) During inspection, this application sends separate GET request to retrieve the image of the product by its name from system directory.
2) Using web proxy like Caido or Burp we can send this request to Replay/Repeater and start testing it. I tried url encoding, double url encoding, and none of these worked for this lab.
3) After doing research, I found out that if web application uses non-recursive filter, then we can use `....//`. This `....//` after filtering deletes the matching `../` part and leaves us with `../` which is still malicious. This way we can bypass this non-recursive filter and retrieve `/etc/passdw` and solve this lab.

---


## Payload / key command
```bash
GET /image?filename=....//....//....//....//....//etc//passwd HTTP/1.1
...
```

---


## What I'd recognize faster next time
Doing research after some attempts is very crucial because there will be always areas that you do not know, which is completely normal. What is important is to do research and learn new stuff to increase your pattern recognition.
 

