# [Blind SQL injection with conditional errors] — [PortSwigger] — [Practitioner]
**Date:** 2026-11-21
 
---
 
## Vulnerability / core concept
Blind SQL Injection

## What made me stuck
At first I had no idea how to return error if substring of password does not match, which kept me in thinking phase.
 
## What unblocked me
After some research I found out that we can use IF non-Oralce and CASE WHEN Oracle and if substring does not match we can return 1/0, which causes error.
 
---


## Attack path
1) First, we need to use `'` to see if we get error because of wrong SQL query syntax.
2) After we confirm SQLi, we can use `CASE WHEN` to compare each character of `administrator` password with arbitrary character a-z, A-Z, and 0-9. If it matches, we return 1 and we get 200 Ok status code. But if it does not match, then we return 1/0, which return 500 Internal Error.
3) After enumerating all combinations using matrix automate from Caido we can filter to have only responses with 200 Ok status code. Then, we can sort our payload to start from 1st character of password and construct it.

---


## Payload / key command
```sql
TrackingId=mIe94oxyeLhSZMcL' AND CASE WHEN (SELECT SUBSTR(password,1,1) FROM users WHERE username='administrator') = 'd' THEN 1 ELSE 1/0 END = 1 --;
```
Here, we should think like `SUBSTR(password,i,1)`, where i will increase after each match. In addition, `d` here is also some arbitrary character that will change from a-z, A-Z, and 0-9 to match the password character.

---


## What I'd recognize faster next time
To retrieve information from table using error-based injection we can use `IF` or `CASE WHEN` depending if dbms is Oracle based or not. The condition to receive error when there is no match would be returning 1/0.
 

