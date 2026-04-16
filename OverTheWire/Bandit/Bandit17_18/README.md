# Description
There are 2 files in the homedirectory: passwords.old and passwords.new. The password for the next level is in passwords.new and is the only line that has been changed between passwords.old and passwords.new

NOTE: if you have solved this level and see ‘Byebye!’ when trying to log into bandit18, this is related to the next level, bandit19
## Analysis
When connecting to `bandit17` we see two files: `passwords.new` and `passwords.old`. To find password for `bandit18` we need to find the changed line in passwords.new.
## Solution
Solution is very simple: we just should use command `diff`:
```bash
diff passwords.new passwords.old
```
This command will find the difference and we will get the following output:
```bash
bandit17@bandit:~$ diff passwords.new passwords.old 
42c42
< x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO
---
> 390zFj2NETFVZkqYw8UEFdN6h40oGVtT
```
As you can see, the x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO is the password for bandit18!
