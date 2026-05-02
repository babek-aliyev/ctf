# [Blind SQL injection with conditional responses] — [PortSwigger] — [Practitioner]
**Date:** 2026-05-02
 
---
 
## Vulnerability / core concept
Blind SQL Injection

## What made me stuck
At first I didn't really understand how to retrieve the data from tables using blind sql injection. However, after some research, I found out that it is not that complicated as I thought it would be.
 
## What unblocked me
To extract data from tables using SQLi, we can boolean or time-based responses.
 
---


## Attack path
1) Use `'` tracking id cookie to validate if we have different behaviour in out application.
2) After validating, we can use both `' and '1'='1` and `' and '1'='2` to check if we have different responses. Also, we can use `sleep(10)` to check if response returns after 10 seconds. Using these methods we confirm that web application is vulnerable to SQLi. The difference in this lab is `Welcome back!` label when query successfully returns any row.
3) As we are given table and columns names in this lab, our next step would be comparing each character of password to list of all characters to find the match. I used Caido Automate for this purpose.


---


## Payload / key command
```
TrackingId=E4qCO2PMPHLUZObu' and (select substring(password,17,1) from users where username = 'administrator')='t
```
This is one of the successful requests in Caido Automate. As you can see, caido automate will take each character in password (in this example its 17th char) and compare it to some character (in this example its 't'). After successful try, it will increase placeholder from 17 to 18 and start enumerating again.

---


## What I'd recognize faster next time
Extracting data from blind sql is not as easy as regular one. It requires patience to find the difference between responses and crafting smart payload that will reveal the data that is needed.
 

