# Bandit Level 11=> Level 12 | OverTheWire
## Description
The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

## Analysis
It is given that all letters in `data.txt` (including lowercase and uppercase) have been rotated by 13 positions. Therefore, when we want to read `data.txt` we get the following output:
```bash
bandit11@bandit:~$ cat data.txt 
Gur cnffjbeq vf 7k16JArUVv5LxVuJfsSVdbbtaHGlw9D4
```
This rotation is a popular encryption method which is called **ROT13**.

## Solution
To decode this `data.txt` file, I used **CyberChef** website, which is ideal for these purposes.

Inside CyberChef we need to choose *ROT13* from left part, input the string/file we want to decode, and press **BAKE!** (it is often set to bake automatically). This is how it should look like:
![](images/intro.png)

This is how we get the password for bandit12!
