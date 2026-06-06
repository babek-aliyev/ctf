# [Insufficient workflow validation] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-06
 
---
 
## Vulnerability / core concept
Insufficient Workflow Validation

## What made me stuck
This level was pretty straightforward, so I was not stuck.
 
## What unblocked me
`null`
 
---


## Attack path
1) First, we need to add some cheap item to our cart, so we can purchase it and get the confirmation GET request from it.
2) After getting confirmation request we add jacket to the cart, and try to buy it. Normally, we get insufficient credit.
3) However, if after POST request of purchasing jacket we send GET confirmation request, server blindly accepts it and we purchase the jacket for free.

---


## Payload / key command
```bash
GET /cart/order-confirmation?order-confirmed=true HTTP/1.1
...
```
We should send this request after POST request of purchasing the jacket.

---


## What I'd recognize faster next time
Sometimes developers do not consider the edge cases when users do not follow their assumptions in workflow. This can lead to a logic flaw that might cost a lot for a business.
 

