# [SQL injection attack, querying the database type and version on MySQL and Microsoft] — [PortSwigger] — [Practitioner]
**Date:** 2026-05-28
 
---
 
## Vulnerability / core concept
SQL injection

## What made me stuck
In this lab I tried to use `ORDER BY 1,2,3 and '1'='1` to find the number of columns in first `SELECT`. However, I missed the idea how that payload would work. I though that this query confirms that there are 3 columns in the first `SELECT`, but it wasn't like that. `ORDER BY 1,2,3 and '1'='1` takes `3 and '1'='1` as a whole expression and it becomes `3 and 1` because `'1'='1'` equals 1. Therefore, `3 and 1` also becomes 1 as it returns true. So the final payload looked like `ORDER BY 1,2,1` which is perfectly fine and does not indicate that there are 3 columns.

## What unblocked me
After testing my query several times and verifying it with AI I found out that I am missing an important nuance in the payload that confused me during lab. Instead of 2 columns I was focusing on 3 columns the whole that, therefore, none of my union commands worked.
 
---


## Attack path
1) Use ' to see if user input is directly put into query and whether it is filtrated
2) Use `' and '1'='1'` and `' and '1'='2` to see any difference between responses. If there is a difference, we confirm SQLi
3) Validate the number of columns in first `SELECT` using `ORDER BY` or `UNION` commands.
4) Use `@@version` to find the version of this dbms

---


## Payload / key command
```bash
'%20union%20select%20@@version,NULL%23
```
Note that payload should be encoded to work, especially `#` character should be represented as `%23` to work.

---


## What I'd recognize faster next time
Should be extra careful next time while using query command such as `ORDER BY 1,2,3 AND '1'='1` as they may work completely different than intentions.

