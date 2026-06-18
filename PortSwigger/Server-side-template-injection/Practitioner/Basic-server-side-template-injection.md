# [Basic server-side template injection] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-18
 
---
 
## Vulnerability / core concept
Server-side Template Injection

## What made me stuck
I got confused at first because I could not find the attack surface. However, after clicking on products I noticed that one product was out of stock which had the attack surface I needed.
 
## What unblocked me
Clicking around.
 
---


## Attack path
1) We are given a e-commerce website that contains multiple products. After careful analysis of it, we can notice that it contains a product which is out of stock.
2) When we press on that product, we get an message at home page saying `Unfortunately this product is out of stock`. This happens through `GET /?message=Unfortunately..` request.
3) We are given that we need to exploit unsafe construction of ERB template. After digging in documentation and other sources, I saw that the syntax for this template is the following: `<%= ... %>` to display output an `<% ... %>` for loops and coniditionals. 
4) To test SSTI, we need to first check whether template executes our expressions. We can use URL encoded version of `<%= 7*7 %>`. We can notice that we get `<div>49</div`: template successfuly executed our payload.
5) Now, we need to create a malicious payload that will delete carlos's `morale.txt` file from his home directory and solve this lab.

---


## Payload / key command
```
GET /?message=%3C%25%3D%20system('rm%20%2Fhome%2Fcarlos%2Fmorale.txt')%20%25%3E HTTP/1.1
...
```
The encoded payload is `<%= system('rm /home/carlos/morale.txt') %>`. This will execute system level command and remove `morale.txt` file from user carlos's home directory.

---


## What I'd recognize faster next time
It is important to check everything in the web application. At first it might seem that there is nothing really to exploit. However, a single not usual case like item is out of stock request can expose critical vulnerability that we wouldn't notice if we did not pay enough attention.


