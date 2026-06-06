# [Authentication bypass via flawed state machine] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-07
 
---
 
## Vulnerability / core concept
Authentication Bypass

## What made me stuck
This level was pretty straighforward, I just tested and found the solution in relatively short amount of time.
 
## What unblocked me
`null`
 
---


## Attack path
1) When we are logging in to our account we can notice that user is forced to select between two roles: `user` and `content-author`.
2) I tried to POST this request while logget out to test if it will default to admin account but it did not work.
3) Then, I decided what will happen if I do not select any role? I just dropped the `GET /role-selector` request, reloaded page and that is it. Application has authentication bypass because if role is not selected, it assigns admin privilege by default.

---


## Payload / key command
After logging in, drop `GET /role-selector` request and refresh page to gain admin privilege by default.

---


## What I'd recognize faster next time
Attacker might simply skip some steps during application workflow that can lead to very serious problems like authentication bypass and privilege escalation.
