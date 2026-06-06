# [Weak isolation on dual-use endpoint] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-06
 
---
 
## Vulnerability / core concept
Weak Isolation on Dual-use Endpoint

## What made me stuck
We could change the password from three different endpoints: `/my-account?id=wiener`, `/my-account/` and `/my-account/change-password`. I was stuck because I tested mainly `/my-account/` endpoint and did not check other endpoints like I did with `/my-account/`.
 
## What unblocked me
Hint from solutions just unlocked me how to solve this problem, I realized that I was missing important part in logic of application. All I had to do is to test `/my-account/change-password`.
 
---


## Attack path
1) We observe a form for updating email and changing password.
2) I tested updating email with lots of things and nothing worked out.
3) I tried to set the password value to ` ` (space) so maybe application will ignore the parameter and skip `current-password` so I can update administrator password, but it did not work out.
4) I noticed that when we write username that does not belong to use, we are navigated to `/my-account/change-password` page. In this page, after some testing, we can observe that if we remove `current-password` field, we can still update the password.
5) All we need to do is set username to `administrator` in `/my-account/change-password` endpoint, and during intercept remove `current-password` field and update the password of administrator.
6) Now we can login administrator account with new credentials and delete user carlos.

---


## Payload / key command
```bash
csrf=P9uSNBK2RU7VjG32hInZD4yGR2986Xes&username=administrator&new-password-1=peter&new-password-2=peter
```
Use this payload at `/my-account/change-password` endpoint.

---


## What I'd recognize faster next time
It is important to check all endpoints throughout testing and apply same methodologies to all of these endpoints. If one endpoints is secure, that does not automatically mean all of them are secure, even if they are doing same logic.


