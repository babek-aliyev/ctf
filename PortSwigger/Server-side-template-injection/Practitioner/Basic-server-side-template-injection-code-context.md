# [Basic server-side template injection (code context)] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-18
 
---
 
## Vulnerability / core concept
Server-side Template Injection

## What made me stuck
This level was pretty solvable, I solved this relatively quickly.
 
## What unblocked me
`null`
 
---


## Attack path
1) First we need to log in so we can increase the attack range of this application. After logging in we need to carefuly inspect the application and see how it works. We can notice that `?my-account=` has `Preffered name` functionality. This functionality changes how our name looks for others. To see our name first we need to make some comment under some post. Now, we can see that changing preffered name changes how our name is displayed for others.
2) When we are inspecting the requests closely, we can notice the following parameter in the `POST /my-account/change-blog-post-author-display HTTP/1.1
` request:
* `blog-post-author-display=user.nickname`
This is a strong indication that this web application uses template that dynamically retrieves users' nicknames. 
3) After seeing this, I started to test this parameter. I changed it to `user.nickname}<dev>` and send the request. After that, I went to blog post to see how my name is display there. There, I got an error saying:
```bash
No handlers could be found for logger "tornado.application" Traceback (most recent call last): File "<string>", line 15, in <module> File "/usr/local/lib/python2.7/dist-packages/tornado/template.py", line 317, in __init__ "exec", dont_inherit=True) File "<string>.generated.py", line 4 _tt_tmp = user.nickname}<div> # <string>:1 ^ SyntaxError: invalid syntax
```
This basically revealed that this web application uses Tornado template with python version 2.7. Moreover, we also got the line that is throwing error which is `_tt_tmp = user.nickname`. Now, after getting all this information, we can start crafting our payload and solve this lab.

---


## Payload / key command
```bash
POST /my-account/change-blog-post-author-display HTTP/1.1
...


blog-post-author-display=__import__('os').popen('rm%20/home/carlos/morale.txt').read()&csrf=XjT4lKzwCy2gcwx36XFhheCVjvj1oLL7
```
This payload will execute in Tornado template and will delete carlos's `morale.txt` file in his home directory.

---


## What I'd recognize faster next time
It is very important to gain as much information about the used stack as we can. The more information a pentester/attacker has, the higher the chances of exploiting the application or server. This is why software engineers are required to hide all error messages that can reveal too much information.

