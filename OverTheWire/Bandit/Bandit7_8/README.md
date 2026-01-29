# Bandit Level 7=> Level 8 | OverTheWire
## Description
The password for the next level is stored in the file data.txt next to the word millionth

## Analysis
This CTF is very easy to complete. After connecting to the server, we need to run command `ls` to see what we have:
```bash
bandit7@bandit:~$ ls
data.txt
```
Now, all we have to do is to use the `grep` command:

```bash
bandit7@bandit:~$ grep millionth data.txt 
millionth       dfwvzFQ---------------------
bandit7@bandit:~$ 
```

In this example, `grep` command takes **millionth** as an input and `data.txt` as filename. This is how we solve the current CTF!!

 
