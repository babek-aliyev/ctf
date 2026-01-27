# Bandit Level 2=>Level 3 | OverTheWire

## Description
The password for the next level is stored in a file called *--spaces in this filename--* located in the home directory
## Analysis
Similar to previous level, in this CTF we should also read a file with a "unusual" name.
## Solution
The `cat` command treats `--spaces in this filename--` symbol as 4 different files. In Unix-bases systems to read files with unusual names we should use single or double quotes to indicate that all these words belong to the name of one file.
## Answer
Now, all we have to do is to run combination of `cat` command with single/double quotes:
```bash
bandit2@bandit:~$ ls
--spaces in this filename--
bandit2@bandit:~$ cat ./"--spaces in this filename--"
-----------------------------------
bandit2@bandit:~$ 
```
Now `cat` command treats `--spaces in this filename--` as one filename and we can read the password for bandit3.


