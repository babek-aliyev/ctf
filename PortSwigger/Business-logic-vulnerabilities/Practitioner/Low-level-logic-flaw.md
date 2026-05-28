# [Low-level logic flaw] — [PortSwigger] — [Practitioner]
**Date:** 2026-05-29
 
---
 
## Vulnerability / core concept
Logic Flaw in Purchasing Workflow 

## What made me stuck
Actually, I found that the when we add too much quantity we get big negative integer. The part that I missed was that this negative number was minimum value of int and it was going down as I added new jackets to the cart.
 
## What unblocked me
I gave my findings to AI and asked for hints. AI suggested me to play with number of items in the cart to see how it changes: is it random or there is some pattern. This helped me to identify the logic flaw.
 
---


## Attack path
1) First, we move around web application to know what it does and how it does.
2) After some recon, we can use proxy tools to inspect requests more closely. During this inspect, nothing extraordinary stood out.
3) I decided to play with quantity number in requests and found out that the quantity can be 99 at maximum. Then I used Automate in Caido to sent tons of requests with quantity 99. I noticed that after some point the price became negative.
4) That negative number was the minimum of int and it was going down as I was adding more and more jackets to the cart.
5) After 32123 jackets, I was the nearest to the 0, but I had to other items to the cart so I can make the price in range from 0 to 100 so I can purchase it.

---


## Payload / key command
Quantity of jacket is 32123
Quantity of "What Do You Meme" is 13

---


## What I'd recognize faster next time
If you find something that does not work properly, there is a high chance that it can be exploitable. Like in this lab, I found almost everything, just small hint from AI helped me to connect this logic flaw with max and min number of int.


