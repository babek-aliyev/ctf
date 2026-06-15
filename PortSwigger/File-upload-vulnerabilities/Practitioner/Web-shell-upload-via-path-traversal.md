# [Web shell upload via path traversal] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-15
 
---
 
## Vulnerability / core concept
Chaining Path Traversal with Unrestricted Upload

## What made me stuck
When I was submitting the file, I used `../` prefix to see if I can upload file to another folder, which will treat `.php` file not as a text but as a code. However, I did not think about encoding `/` which led me to rabbithole.
 
## What unblocked me
After I used a small hint, I solved this lab with pokerface.
 
---


## Attack path
1) First, we need to login to our account to have file upload access.
2) During inspection, I noticed that we can upload file with `.php` extension and application accepted it and put it in `/files/avatars/filename.php`. 
3) I tried to access `/files/avatars/filename.php` and received my `.php` payload in form of text, which is not very helpful to us. Then I tried to access `/files/` and `/files/avatars` but they were givin me 403 forbidden.
4) I tried lots of things, including testing commenting section, post section, resources, etc. The first thing I tried was adding `../` in front of filename so I can upload my payload into different folder than `/avatars`. My assumption was that `/avatars` folder does not allow execution of any files inside it.
5) I was thinking correct. BUT! Because simply I did not try to encode the `../` to bypass path traversal restriction. This lead me to testing the whole application without success. I even tried to overwrite `/home/carlos/secret` so maybe it will work for me.
6) After encoding `../filename.php` into `..%2filename.php`, my payload got uploaded into `/files/` folder and I could execute it as I assumed. Now we can retrieve `/home/carlos/secret` and solve this lab.

---


## Payload / key command
When pressing upload, we should intercept the requets and add `..%2` to the start of our filename.

My payload was:
```php
<?php echo system($_GET['command']); ?>
```
Then, I visited `/files/filename.php?command=cat%20/home/carlos/secret` to retrieve the flag and solve lab.

---


## What I'd recognize faster next time
While trying to focus on one vulnerability, it is ALWAYS important to remember that we can chaing it with other vulnerabilities. Moreover, it is important to rememeber the bypass techniques of other vulnerabilities and not move on after first unsuccessful attempt.
 

