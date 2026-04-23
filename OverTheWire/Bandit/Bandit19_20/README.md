# Bandit Level 19=> Level 20 | OverTheWire

## Description
To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.

## Analysis
After connecting to the `bandit20` machine, we can list it contents using `ls` command and find this:
```bash
bandit19@bandit:~$ ls
bandit20-do
```
As this level is about `setuid` and `setgid` we can run `ls -la` to see all files with their permissions:
```bash
bandit19@bandit:~$ ls -la
total 36
drwxr-xr-x   2 root     root      4096 Apr  3 15:17 .
drwxr-xr-x 150 root     root      4096 Apr  3 15:20 ..
-rwsr-x---   1 bandit20 bandit19 14888 Apr  3 15:17 bandit20-do
-rw-r--r--   1 root     root       220 Mar 31  2024 .bash_logout
-rw-r--r--   1 root     root      3851 Apr  3 15:10 .bashrc
-rw-r--r--   1 root     root       807 Mar 31  2024 .profile
```
Here we see that it is possible to use execute `bandit20-do` as `bandit20` because of `setuid`. Basically, `setuid` allows users to execute files with owner privileges. It is a useful thing that is used by in file permission management like editing password that changes `/usr/bin/passwd` or using command `ping` to test network. Without `setuid` ordinary user won't have permissions to execute those actions.
## Solution
As description says we should first execute the binary executable without arguments to find out its usage:
```bash
bandit19@bandit:~$ ./bandit20-do 
Run a command as another user.
  Example: ./bandit20-do whoami
```
When I tried to run `./bandit20-do whoami` I got `bandit20` as a response. From there I assumed that this binary executable helps us to execute commands with `bandit20` permissions. Havind this assumption I tried the following command and it worked:
```bash
bandit19@bandit:~$ ./bandit20-do cat /etc/bandit_pass/bandit20 
0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
```
This is how we solve this ctf!

