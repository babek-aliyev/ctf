# [Blind SQL injection with time delays] — [PortSwigger] — [Practitioner]
**Date:** 2026-05-06
 
---
 
## Vulnerability / core concept
Blind SQL Injection

## What made me stuck
I tried all types of databases and their time-based injections but couldn't find the one. The main issue was in using `AND "injection code"` like `AND 1=pg_sleep(10) --` for PostgreSQL. I did not know that we cannot compare `pg_sleep(10)=1` as `pg_sleep` returns void.
 
## What unblocked me
The proper way of using that would differentiate based on dbms. For example, for PostgreSQL we need to use `pg_sleep(10) is not null` because `pg_sleep` returns void and we cannot compare it with 1 like i did before.
 
---


## Attack path
1) To exploit this website, all we need to do is simply brute-force through all database time-based injections to see if we can get delayed response.


---


## Payload / key command
```sql
TrackingId=BYkdgkeb4vIgK89h'|| (select pg_sleep(10)) --
```
In this payload, `pg_sleep(10)` becomes void. Therefore, concatenating it does not change the original tracking id but executes time-based injection.

Note: After some research I found another payload that works for this lab:
```sql
TrackingId=BYkdgkeb4vIgK89h' AND pg_sleep(10) IS NOT NULL --
```

---


## What I'd recognize faster next time
When we are in string context like this tracking id, on top of `AND` we can use `||`, which appears more clean. So, if `WHERE` filter is in number context like integer (`where id=1`) we should use `AND` as `||` will not give us anything because 1 is not string. But when we are in string context, we can try both `AND` and `||` to see if we can use time-based injection. Moreover, sleep functions in different dbms return different values and it is essential to know them.
 

