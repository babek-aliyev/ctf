# Bandit Level 14=> Level 15 | OverTheWire
## Description
The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost.
## Analysis
After connecting to `bandit14` machine, we can observer that there is no files that we can use for further exploitation. We are given that we need to submit the password of `bandit14` to port 30000. It is also possible to run simple command `nmap` to see active ports on `bandit14` machine:
```bash
bandit14@bandit:~$ nmap 127.0.0.1
Starting Nmap 7.94SVN ( https://nmap.org ) at 2026-04-16 17:46 UTC
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00016s latency).
Not shown: 993 closed tcp ports (conn-refused)
PORT      STATE SERVICE
22/tcp    open  ssh
1111/tcp  open  lmsocialserver
1840/tcp  open  netopia-vo2
4321/tcp  open  rwhois
8000/tcp  open  http-alt
30000/tcp open  ndmps
50001/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 0.06 seconds
```
## Solution
To solve this problem we should use basic command `nc`: it will connect to the port that we want. We can also add text as an input to it through piping and therefore solve this level by using the following command:
```bash
bandit14@bandit:~$ echo MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS | nc 127.0.0.1 30000
Correct!
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo

```

This is how we get password for `bandit15`!
