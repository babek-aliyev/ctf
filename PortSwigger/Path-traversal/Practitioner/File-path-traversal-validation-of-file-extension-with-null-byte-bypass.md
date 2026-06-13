# [File path traversal, validation of file extension with null byte bypass] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-13
 
---
 
## Vulnerability / core concept
Path Traversal

## What made me stuck
This level was easy for me because I read article about bypassing extension using null byte.
 
## What unblocked me
`null`
 
---


## Attack path
1) During inspection of web application, we can notice that it sends GET request to retrieve image of the product. This web application does this using filename of the image.
2) After some testing using Replay, I noticed that the defence depends on whether filename contains extension or not. I recently read how we can use null byte to bypass this extension checking filter. Basically, we can append null byte (%00) before `.extension`. This way application validates that filename has the required extension, while server does not see that extension because server sees null byte as a string terminator. This way we bypass validation of file extension, access `/etc/passwd` and solve this lab.

---


## Payload / key command
```bash
GET /image?filename=../../../../../etc/passwd%00.jpg HTTP/1.1
...
```

---


## What I'd recognize faster next time
Security measures that are based on checking whether filename contains some specific extension or base path are very unreliable because they can be easily bypassed by attackers. You should always resolve real path and check where it actually lands.

