# [SQL injection UNION attack, determining the number of columns returned by the query] — [PortSwigger] — [Practitioner]
**Date:** 2026-04-29
 
---
 
## Vulnerability / core concept
SQL Injection

## What made me stuck
The acceptance method got me quite confused as I did not get what should I do exacly in this lab. I was even searching tables and columns to retrieve some data.

## What unblocked me
This lab was much more simpler that I thought: we should have just determined the number of columns by using specifically `union select` with null values. 

---


## Attack path
1) Use `'` to see how web app responses to it. If it reacts differently, like with error message in our case, that means it can be vulnerable to sql injection
2) To confirm it, we can use `' and '1'='1` and `' and '2'='1` and see if there any difference in responses
3) After confirming, we should determine the number of columns used in first `select` by using `union select null --` and increase number of nulls until we get proper response from web application. We can also use `order by`, but this lab specifically required to use `union select`.

---


## Payload / key command
```sql
filter?category=Gifts' union select null, null, null --
```

---


## What I'd recognize faster next time
Would recognize that type of acceptance faster for sure!

