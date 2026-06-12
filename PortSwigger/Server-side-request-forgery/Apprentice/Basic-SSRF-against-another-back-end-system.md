# [Basic SSRF against another back-end system] — [PortSwigger] — [Apprentice]
**Date:** 2026-06-12
 
---
 
## Vulnerability / core concept
Server-side Request Forgery

## What made me stuck
Nothing, this level was pretty straightforward, i solved it quickly.
 
## What unblocked me
`null`
 
---


## Attack path
1) In this application, during inspection via web proxy, we can notice that application sends request to its internal server to get available stock for an item.
2) As we can notice, it uses IP address + enpoint to find amount of product.3) When I changed IP address from `192.168.0.1` to `192.168.0.x` i got 500 internal error. That gave me an idea to try to iterate IP addresses maybe i will find something interesting.
4) I used Automate in Caido and tested IP addresses from `192.168.0.2` to `192.168.0.255`. During iteration, in my case, i found out that `192.168.0.250` gave me 404 not found error.
5) After seeing that error i immediately understood that this IP address is not related to checking stock because it does not have product endpoint.
6) Using Replay, i started analyzing `192.168.0.250` ip address. I deleted the existing `/product/stock/check?productId=2&storeId=1` with `/admin` and it worked! In response I got html code for admin account.
7) There I noticed `http://192.168.0.250:8080/admin/delete?username=carlos` and sending that request deleted user carlos and solved this lab.

---


## Payload / key command
```bash
http://192.168.0.250:8080/admin/delete?username=carlos
```

---


## What I'd recognize faster next time
It is important to observe application very closely. If we find some unprotected request to internal server, this leads to critical vulnerability.


