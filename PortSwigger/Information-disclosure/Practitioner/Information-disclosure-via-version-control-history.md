# [Information disclosure in version control history] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-21
 
---
 
## Vulnerability / core concept
Information Disclosure

## What made me stuck
At first I tried to find and inspect everything in the browser, which obviously did not give me any results.

## What unblocked me
After a little bit of digging, I found a tool that made my job much more easier.
 
---


## Attack path
1) During inspection, we can see that there is almost nothing that reveals any information.
2) I searched for `robots.txt` and `sitemap.xml` too still no results. Then I decided to check for `/.git` and it worked! I was able to see the commit logs and who made those commits. 
3) I tried to find any information using web browser but it just didn't work. Later, I found out a tool that made my job 100x easier: `git-dumper`. I downloaded it and cloned that `/.git` locally and started inspecting it.
4) Checking that git branch, I was at the head of master, where last commit removed the password for admin. I checked the logs to see the commits using `git log` command and found out the hash of the very first commit that contained the password of admin.
5) Now, all I have to do is use `git checkout commit-hash` command and go back to the initial repo state. Then, we can check for `admin.conf` file and get the password, log in as administrator and delete user carlos to solve this lab.

---


## Payload / key command
```bash
git-dumper https://0a8300a203f10798818d613500f10067.web-security-academy.net/.git/ port-git
```

Check log for first commit hash using `git log`.
Then switch to that commit using `git checkout commit-hash` command. Now you can see the admin password in the `admin.conf` file.

---


## What I'd recognize faster next time
It is very important to use tools that can make our pentesting much easier and save us tons of time. Therefore, always check for useful tools that are available to us as pentesters.



