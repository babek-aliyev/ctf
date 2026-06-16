# [Blind OS command injection with time delays] — [PortSwigger] — [Practitioer]
**Date:** 2026-06-16
 
---
 
## Vulnerability / core concept
OS Command Injection

## What made me stuck
Nothing, I was able to solve this lab by using my knowledge and leveraging AI.
## What unblocked me
`null`
 
---


## Attack path
1) During inspection of web application, we can notice that web application has `Submit feedback` functionality that sends email to web app employees I guess.
2) We intercept and send `Submit feedback` to Replay in Caido to start analyzing it. We can notice that when we are sending the feedback we get only `{}` as a response. No matter what we do in that request, it does not get displayed in response. The only thing I could get was `Could not save` that did not really help.
3) I asked AI to explain and show me how usually web applications handle email functionality using system. It returned me an example shell script, that made me understand the underlying system much better.
4) From this moment I started to leverage AI to find ways to bypass vulnerable shell script. As a result, I was able to execute a 10-second time delay and solve the lab.

---


## Payload / key command
Using AI, I developed a mental model of how feedback systems often invoke operating-system commands to send emails. The exact implementation of the lab is unknown, but it is likely that user-controlled input was being incorporated into a shell command without proper escaping.
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
From here, I started to find ways to exploit this script and see if it actually works with the actual web application too. As a result, I crafted the following payload for `subject` field.
```bash
"; sleep 10; echo "
```
After pasting URL encoded version of this payload into subject field, we effectively end first command `mail` with empty string and `;`, execute our `sleep 10` and again end it with `;`, and finally use `echo` with empty `""` to avoid errors that might prevent our sleep command to execute.

---


## What I'd recognize faster next time
AI is very helpful to explain systems, scripts and much more and helps a lot with visualizing a problem and its possible vulnerabilities.


