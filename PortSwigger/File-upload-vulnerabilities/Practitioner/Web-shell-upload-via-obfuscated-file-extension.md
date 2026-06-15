# [Web shell upload via obfuscated file extension] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-16
 
---
 
## Vulnerability / core concept
Web shell upload via obfuscated file extension

## What made me stuck
Nothing, this level was pretty easy and I solved it quickly.
 
## What unblocked me
`null`
 
---


## Attack path
1) First we need to log in to access file upload functionality.
2) During inspection, we can notice that we cannot upload a file with `.php` extension: web application effectively filters it.
3) I tried to write extension as `.pHp`, however, it still did not work for me. The next thing that came to my mind was using null byte. 
4) I decided to upload file using `.php%00.jpg` extension. My idea is null byte showing the end of string and `.jpg` will be truncated. When I pressed upload, it got uploaded successfuly. However, when I accessed `/files/avatars/webshell.php%00.jpg`, I got Apache error. Then, I decided to remove `%00.jpg` and leave only `webshell.php` and it worked! I received `/home/carlos/secret` and solved the lab.

---


## Payload / key command
My `webshell.php` payload is the following:
```php
<?php echo file_get_contents('/home/carlos/secret'); ?>
```
We should submit this file with new obfuscated extension `.php%00.jpg`.

---


## What I'd recognize faster next time
We should use as much obfuscation techniques as we know. If web application uses blacklist-based filtration, that means there is a chance that we will be able to bypass that filtration and upload malicious payload that can lead to RCE.


