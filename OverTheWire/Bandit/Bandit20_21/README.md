# Bandit Level 20=> Level 21 | OverTheWire

## Description
There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

NOTE: Try connecting to your own network daemon to see if it works as you think

## Analysis
In this `bandit20` machine we can see the following file:
```bash
bandit20@bandit:~$ ls
suconnect
```
Using `ls -la` we can see permissions of this file:
```bash
bandit20@bandit:~$ ls -la
total 36
drwxr-xr-x   2 root     root      4096 Apr  3 15:17 .
drwxr-xr-x 150 root     root      4096 Apr  3 15:20 ..
-rw-r--r--   1 root     root       220 Mar 31  2024 .bash_logout
-rw-r--r--   1 root     root      3851 Apr  3 15:10 .bashrc
-rw-r--r--   1 root     root       807 Mar 31  2024 .profile
-rwsr-x---   1 bandit21 bandit20 15612 Apr  3 15:17 suconnect
```
As you can see `suconnect` is `setuid` binary and can be executes as its owner `bandit21`.
## Solution 
To solve this lab we need to implement several simple steps.
1) First we need listen to some port by using `nc` command:
```bash
bandit20@bandit:~$ nc -l -p 12345


```
Here `-l` stands for `listen` and `-p` stands for port.

Now it is time to run `suconnect` binary and connect it to local 12345 port:
```bash
bandit20@bandit:~$ ./suconnect 12345

```

As you can see, now `suconnect` acts like a client and waits for a response from a server. The server in our case is localhost on port 12345. All we got to do now is to send the password of `bandit20` as a server to client and retrieve the password for `bandit21`:
```bash
bandit20@bandit:~$ nc -l -p 12345
0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
EeoULMCra2q0dSkYj561DX7s1CpBuOBt
```

On the client side we get this output:
```bash
bandit20@bandit:~$ ./suconnect 12345
Read: 0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
Password matches, sending next password
```
This is how we solve this ctf!!


