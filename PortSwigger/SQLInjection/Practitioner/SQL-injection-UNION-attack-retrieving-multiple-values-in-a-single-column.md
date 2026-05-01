# [SQL injection UNION attack, retrieving multiple values in a single column] — [PortSwigger] — [Practitioner]
**Date:** 2026-05-02
 
---
 
## Vulnerability / core concept
SQL Injection

## What made me stuck
I could only retrieve either password or username using union. However, it was hard to match username and password pair.
 
## What unblocked me
After some research I found out that we can concatenate string values in several columns and combine them into one.
 
---


## Attack path
1) Use `'` to determine if web application returns different response than normal like error message, etc.
2) Use `' and '1'='1` and `' and '1'='2` to see if there is any difference between responses that web application responds to client. If there is a difference, that means we confirm sql injection.
3) Use `order by` to determine the number of columns in the first `select` so we can use union injection.
4) After determining number of columns in first select, we use `union select` with different column types like string and integer to find the matching column types.
5) After finding that second column matches with string type, we can concatenate username and password into one column and retrieve both data at the same time.



---


## Payload / key command
```sql
' union select 1, CONCAT(username, ' -> ', password) FROM users --
```

---


## What I'd recognize faster next time
If we can retrieve only one column because of column type and we need more, we can use built-in concatenate function in SQL to combine several columns into one.
 

