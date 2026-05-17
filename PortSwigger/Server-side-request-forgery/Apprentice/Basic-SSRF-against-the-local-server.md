# [Basic SSRF against the local server] — [PortSwigger] — [Apprentice]
**Date:** 2026-05-17
 
---
 
## Vulnerability / core concept
Server-side Request Forgery
## What made me stuck
This level was pretty easy, so there was nothing to get stuck on.
 
## What unblocked me
`null`
 
---
## Attack path
1) After inspecting `/product?product=x` endpoint using Burp Suite or Caido, we can observe that the request fetches a `stockApi` internal server to check the stock.
2) By modifying this internal server link to a malicious `http://localhost/admin` and encoding it, we can now send requests to the internal server.
3) Using Repeater, we send the first request using `http://localhost/admin` and see the following output:
```html
<a href="/admin/delete?username=carlos">
```
4) Now, all we need to do is change our malicious link to `http://localhost/admin/delete?username=carlos` and send the request to the internal server to delete user `carlos`.

---
## Payload / key command
```bash
stockApi=http%3A%2F%2Flocalhost%2Fadmin%2Fdelete%3Fusername%3Dcarlos
```

> **Note:** Only the colon was encoded in the original payload (`http%3a//localhost/...`), leaving `//`, `/`, and `?` raw. That works in most parsers, but fully encoding the URL is more reliable against stricter backends. The payload above uses complete percent-encoding.

---
## What I'd recognize faster next time
- The key signal here was a **user-supplied URL parameter hitting a backend service**. Any time you see a parameter that looks like it's fetching a remote resource (`stockApi`, `url=`, `imageUrl=`, `webhook=`, etc.), SSRF is the first thing to test.
- Sending malicious requests to the internal server may give attackers unauthorized access to privileged endpoints.
