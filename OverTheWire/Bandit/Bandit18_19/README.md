# Bandit Level 18=> Level 19 | OverTheWire

## Description
The password for the next level is stored in a file readme in the homedirectory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH.

## Analysis
When we are trying to login to the machine `bandit18`, we get the following output:
```bash
...

Byebye !
Connection to bandit.labs.overthewire.org closed.
```
We can observe that the bash terminal of machine `bandit18` is modified to log out us when we try to log in using SSH.
## Solution
Solution to this ctf is actually very easy: we just need to execute commands remotely via ssh without fully loggin in. To do so we can use the following command template:
```bash
ssh -p 2220 bandit18@bandit.labs.overthewire.org "some-command"
```
For example, to execute `ls` command we should run the following command:
```bash
ssh -p 2220 bandit18bandit.labs.overthewire.org "ls"
```
This is the output we get after entering password for `bandit18`:
```bash
bandit18@bandit.labs.overthewire.org's password: 
readme
```
Now all we need to do is to read the content of `readme`:
```bash
ssh -p 2220 bandit18@bandit.labs.overthewire.org "cat readme"
```
This is the output for this command:
```bash
bandit18@bandit.labs.overthewire.org's password: 
cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8
```

This is how we solve this ctf!
