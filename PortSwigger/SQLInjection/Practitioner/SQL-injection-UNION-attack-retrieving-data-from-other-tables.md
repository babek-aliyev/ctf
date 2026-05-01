# [SQL injection UNION attack, retrieving data from other tables] — [PortSwigger] — [Practitioner]
**Date:** 2026-05-01
 
---
 
## Vulnerability / core concept
SQL injection

## What made me stuck
This level was quite easy, there was nothing that made me stuck.
 
## What unblocked me
Nothing, it was an easy level to solve.
 
---


## Attack path
1) Use `'` to determine if web application returns different response than normal like error message, etc.
2) Use `' and '1'='1` and `' and '1'='2` to see if there is any difference between responses that web application responds to client. If there is a difference, that means we confirm sql injection.
3) Use `order by` to determine the number of columns in the first `select` so we can use union injection.
4) After determining number of columns in first select, we just use given table name and column names.

---


## Payload / key command
```sql
/filter?category=Pets' union select username, password from users --
```

---


## What I'd recognize faster next time
As I said before, this level was pretty easy.

