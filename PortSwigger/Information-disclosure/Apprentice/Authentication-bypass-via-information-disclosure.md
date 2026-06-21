# [Authentication bypass via information disclosure] — [PortSwigger] — [Apprentice]
**Date:** 2026-06-21
 
---
 
## Vulnerability / core concept
Information Disclosure

## What made me stuck
There was a new concept for me which I did not know before.

## What unblocked me
After some research I was able to finish this lab.
 
---


## Attack path
1) During inspection, I could not find anything that reveals any information. I found that there exists `/admin` path, but it give us 403 forbidden and says only admin interface is available only for local users.
2) I had to do research about ways of finding information disclosure and what ways pentesters are using.
3) I came across a method that I did not know before: using HTTP `TRACE` method that is used for diagnostic purposes. It sends the request that we sent back to us in response.
4) Using this TRACE method, we can see that there is custom HTTP header that we did not know before: `X-Custom-IP-Authorization`.
5) Now, having this information, we can chain it with our previous finding: `/admin` path. We intercept the request and add this new HTTP header set to `127.0.0.1` which stands for local IP address and send that request. We see that we got the access to admin interface successfully. 
6) Now, we need to delete user carlos again using that custom header and solve this lab.

---


## Payload / key command
```bash
GET /admin HTTP/1.1
...

X-Custom-IP-Authorization: 127.0.0.1
```
And then we need to send the following request:
```bash
GET /admin/delete?username=carlos HTTP/1.1
...

X-Custom-IP-Authorization: 127.0.0.1
```



---


## What I'd recognize faster next time
It is very important to research ways of gaining as much information as we can. Like in this lab, if I did not find out TRACE method, I would not be able to exploit admin panel.



