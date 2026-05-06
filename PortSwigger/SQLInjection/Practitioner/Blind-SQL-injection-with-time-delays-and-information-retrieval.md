# [Blind SQL injection with time delays and information retrieval] — [PortSwigger] — [Practitioner]
**Date:** 2026-05-06
 
---
 
## Vulnerability / core concept
Blind SQL Injection

## What made me stuck
This level actually pretty straightforward. I just spent some time trying to use injection using `AND` and `OR` that did not work.
 
## What unblocked me
After some research I figured out that the best way to use my particular SQL injection was finising line with `;` instead of AND and OR.
 
---


## Attack path
1) To confirm sql injection, I used `'|| pg_sleep(10) --` to check whether application retrieves row synchronously and whether is it vulnerable to sql injection. Aften injection i got response with 10 second delay, therefore, i confirmed that sql injection does exist.
2) After confirming sql injection we create a conditional query that will check whether characters of password match with any character from a-z, A-Z, 0-9 using enumeration. To confirm the match, we use 10 second delay and filter the responses based on their roundtrip time.

---


## Payload / key command
```sql
TrackingId=u'%3B%20SELECT%20CASE%20WHEN%20((select%20substring(password%2C1%2C1)%20from%20users%20where%20username%20%3D%20'administrator')%3D'a')%20THEN%20pg_sleep(10)%20ELSE%20pg_sleep(0)%20END%20--
```
We need to encode this payload, because using `;` character will try to add new value to the cookie header.


---


## What I'd recognize faster next time
Sometimes to make injection it is better to use end of line with characters like `;` instead of trying to make a boolean expression using `AND` and `OR`. 
 

