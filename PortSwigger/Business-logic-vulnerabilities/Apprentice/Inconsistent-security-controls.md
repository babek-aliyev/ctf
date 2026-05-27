# [Inconsistent security controls] — [PortSwigger] — [Apprentice]
**Date:** 2026-05-28
 
---
 
## Vulnerability / core concept
Inconsistent Security Controls

## What made me stuck
This level was pretty straighforward and easy, so I did not get stuck.
 
## What unblocked me
`null`
 
---


## Attack path
1) We should move to the `/register` page and register with some arbitrary email (we can use Email Client on the top of page to receive a confirmation link)
2) Now, we can observe the Update Email functionality. We remember that during registration we saw a `If you work for DontWannaCry, please use your @dontwannacry.com email address` message. Now, we need to try to change our email to DontWannaCry company email.
3) After we write `admin@dontwannacry.com` and press update, we can see that we successfully changed our email without verification code. Now we can access admin panel and delete user carlos.

*Note: After solving this lab I checked their solution and they first did a content discovery via enumeration, and after finding `/admin` page, they started to exploit.**

---


## Payload / key command
Update email to this:
```bash
admin@dontwannacry.com
```


---


## What I'd recognize faster next time
It is important to check the security and verification system at all parts of web application as some of these dangerous actions may miss security controls.


