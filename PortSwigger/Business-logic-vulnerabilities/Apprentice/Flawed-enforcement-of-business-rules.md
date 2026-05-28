# [Flawed enforcement of business rules] — [PortSwigger] — [Apprentice]
**Date:** 2026-05-28
 
---
 
## Vulnerability / core concept
Flawed Coupon Rules

## What made me stuck
I tried everything what I could, read multiple articles, common coupon vulnerabilities, and nothing helped. After all of these, I decided to get some hint.
 
## What unblocked me
THERE WAS A SIGN UP BUTTON ON THE BOTTOM OF THE PAGE THAT I DID NOT EVEN NOTICE. After seeing that signup button, this lab become very easy to exploit.
 
---


## Attack path
1) When we enter the page we see that new customers can use NEWCUST5 coupon to get a discount on an item. However, we can use it only once.
2) If you go down on page, you can see a newsletter signup button, that gives you new SIGNUP30 coupon.
3) When we try same coupon twice in a row, we get coupon is already applied error. However, when we try to alternate between them, we can see that we can bypass that security rule.
4) Now, all we need to do is alternate between coupons until the price is below our Store Credit.

---


## Payload / key command
Alternate coupons:
`SIGNUP30`,
`NEWCUST5`

---


## What I'd recognize faster next time
ALWAYS check the full website before trying to find vulnerability. It is important to know all details, as they help you build a much better picture of application.
 

