# [SQL injection UNION attack, finding a column containing text] — [PortSwigger] — [Practitioner]
**Date:** 2026-04-30
 
---
 
## Vulnerability / core concept
SQL Injection

## What made me stuck
This level was pretty straightforward, so I finished really quick without being stuck.

## What unblocked me
There was small description under lab that required specific string to be returned. I was using `'test'` before.
 
---


## Attack path
1) Use `'` to see if web application responses differently to it. If yes, there is a good chance of sql injection
2) To confirm sqli, we can use `' and '1'='1` and `' and '1'='2` to see if there is difference between these two responses. If yes, we just confirmed sqli
3) Use `union select` or `order by` commands to determine number of columns if the first `select`
4) For this specific lab after finding out number of columns is 3, use `union select 'aRGpCT', null, null --`, `union select null, 'aRGpCT', null --`, etc. to find column compatible with string type


---


## Payload / key command
```sql
/filter?category=Pets' union select null, 'aRGpCT', null --
```

---


## What I'd recognize faster next time
It is important to read description carefully, because even you find vulnerability and expose it, it won't be accepted without specific requirements.
 

