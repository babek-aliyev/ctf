# [Infinite money logic flaw] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-07
 
---
 
## Vulnerability / core concept
Infinite Money Logic Flaw

## What made me stuck
I did not know that we can purchase some item from store and actually use it for our exploit purpose.
 
## What unblocked me
After confirming that we can buy gift card from store and use it, this level become quite simple.
 
---


## Attack path
1) First, we need to log in to be able purchase items from store.
2) This application gives infinite SIGNUP30 coupons.
3) Combining these infinite SIGNUP30 coupons, we can purchase 10 usd gift cards for 7 dollar each, which leaves us 3 dollar clean profit.
4) Now all we have to do is to repeat the process multiple times so we can affort to buy jacket and complete this level.

Note: This process can be done manually (this is what I have done), but also it can be automated via Burps macro, caido workflow, or python script using requests.

---


## Payload / key command
Buy discounted gift cards and use them to increase the balance.

---


## What I'd recognize faster next time
It is important to keep in mind that attackers can use literally anything like buying from gift cards from store to exploit the same store application. That is why it is essential to have proper logical workflow in applications.
 

