# [Excessive trust in client-side controls] — [PortSwigger] — [Apprentice]
**Date:** 2026-05-28
 
---
 
## Vulnerability / core concept
Unvalidated User Input

## What made me stuck
This level was pretty easy, so I was not stuck at anything.
 
## What unblocked me
`null`
 
---


## Attack path
1) First we manually go around web app to learn its logic and how it works.2) After we understood the logic behind the web application, it is time for proxy tools to inspect requests more closely.
3) In this lab, we can observe that when we add new item to the cart, it sends its price in the request.
4) Modify this price to anything (except zero, I tried it, item was not added to the cart) that is less than our store credit and you can buy that item.

---


## Payload / key command
```bash
productId=1&redir=PRODUCT&quantity=1&price=100
```
Here, `price=100` means that we set the price of item to 1 dollar (price is sent in cents).

---


## What I'd recognize faster next time
It is important to understand the functionality of the web application first before diving deeper into requests and responses.


