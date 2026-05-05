# [Visible error-based SQL injection] — [PortSwigger] — [Practitioner]
**Date:** 2026-11-21
 
---
 
## Vulnerability / core concept
Blind SQL Injection

## What made me stuck
I solved this lab using `LIMIT 1` to get first entry in username table. I did get administrator and retrieved password for it. But I was questioning whether this is good approach because what if `administrator` is not first user in the table. Then we have to use `OFFSET` but this lab had input length constraint so it was not possible to use that.
 
## What unblocked me
After solving it, I checked how they explain this level, and to my surprise they did it exactly like I did. I guess this lab was specifically designed to have `administator` as first user.
 
---


## Attack path
1) Use `'` to check whether you get different response, if yes, possible SQL Injection.
2) Confirm it using `' and '1'='1` and `' and '1'='2` and check whether you get different responses or not, if yes, you confirmed sql injection.
3) In this lab, `TrackingId` has constrained length, so I deleted the value of `TrackingId` to get extra input space. Then I checked what database I am dealing with by using `' and 1=cast((select version()) as int) --`. This way we determined that it is non-Oracle database.
4) Finally, to solve this lab we retrieved first rows from `username` and `password` columnes and used their value to login as an administrator.

---


## Payload / key command
`' and 1=cast((select username from users limit 1) as int) --`

and 

`' and 1=cast((select password from users limit 1) as int) --`
This way after finding out that first row is `administrator` we can find the password for administrator.

---


## What I'd recognize faster next time
To exploit a web application it is not always important to find best query that will work all the time. Sometimes, if it works, then it works.


