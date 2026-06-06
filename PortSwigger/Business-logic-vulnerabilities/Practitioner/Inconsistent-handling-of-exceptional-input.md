# [Inconsistent handling of exceptional input] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-06
 
---
 
## Vulnerability / core concept
Unvalidated User Input

## What made me stuck
At first I thought we should exploit this lab using sending phishing mail to victim, so I spend quite some time trying it.
 
## What unblocked me
After using some hint, I understood that this lab has nothing to do with phishing.
 
---


## Attack path
1) We know that we should access admin privileges, and to do so we should register using `@dontwannacry.com` email address.
2) After trying some methods, we can observe that we can add `dontwannacry.com` as a subdomain to our attacker email and it will still work. However, we still do not get the admin privilege.
3) When we parse very long string before @, we can see that our email gets truncated. The reason of this is likely email is set to VARCHAR(256) in the database, so anything more than 256 in length gets truncated.
4) Now, all we need to do is craft an email with length so our truncated email ends on `@dontwannacry.com`

---


## Payload / key command
```bash
aexploitb0a77006e04bff16580513ed0014c0078abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ab123456789@dontwannacry.com.exploit-0a77006e04bff16580513ed0014c0078.exploit-server.net
```
Use this email to have `@dontwannacry.com` at the end

---


## What I'd recognize faster next time
Always validate user input. It is also a great idea to have additional input validation in database as well.


