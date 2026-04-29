# [SQL injection attack, listing the database contents on Oracle] — [PortSwigger] — [Practitioner]
**Date:** 2026-04-29
 
---
 
## Vulnerability / core concept
SQL Injection

## What made me stuck
I know how to implement SQL Injection using `sqlmap`. But doing it manually required some research.

## What unblocked me
After reading about `all_tables` and `all_tab_columns` for non-Oracle databases, it went pretty easy.

---


## Attack path
1) Use `'` to verify if server respond with some unexpected response or error. In this lab server responded with error
2) To confirm SQL injection we can use `and '1'='1` and `and '2'='1` to see if there is any difference between responsed. If there is, like in our case, we confirm that web application is vulnerable to sql injection
3) My third step was to confirm number of columns in first `select` by using command `order by 2`. `order by 3` did not work, therefore, we confirmed that we need only 2 columns for our `union select` injection
4) 4th step is get more information about database by using `all_tables` and `all_tab_columns` for Oracle databases.
5) After some enumeration between tables and columns we find out that this database has table called `USERS_XLDSYK`, which has columns `USERNAME_FOYIFU` and `PASSWORD_ZQJFUF`. I did it using `/filter?category=Accessories' union select column_name, null from all_tab_columns where table_name = 'USERS_XLDSYK' --`
6) Now all we need to do is to query this table and find usernames and passwords


---


## Payload / key command
```sql
/filter?category=Accessories' union select USERNAME_FOYIFU, PASSWORD_ZQJFUF from USERS_XLDSYK --
```
Note: table and column names will be different in your case as random part changes.

---


## What I'd recognize faster next time
For manual iteration information about database is essential. To do so we can use `all_tables` and `all_tab_columns` for Oracle databases. I also searched for non-Oracle: use `information_schema.tables` and `information_schema.columns`.

