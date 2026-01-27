# Bandit Level 4=> Level 5 | OvertheWire
## Description
The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command.

## Analysis
When we are connected to the machine, we can run `ls` command to see what files/folders we have:
```bash
bandit4@bandit:~$ ls
inhere
bandit4@bandit:~$ 
```

Then we move to the `inhere` folder and check its content:
```bash 
bandit4@bandit:~$ cd inhere/
bandit4@bandit:~/inhere$ ls
-file00  -file01  -file02  -file03  -file04  -file05  -file06  -file07  -file08  -file09
```
## Solution
Firstly, I just tried to use `cat` command to open all the files manually because the number of files were not that big:
```bash
bandit4@bandit:~/inhere$ cat ./-file01
���0��w�8���q����Y���d����ZCF��+bandit4@bandit:~/inhere$ cat ./-file02
���     L����Q�.��`▒/▒��r
�P{bandit4@bandit:~/inhere$ cat ./-file03
���?�▒��1'�JV����,��2��
                       f�=����bandit4@bandit:~/inhere$ cat ./-file04
��us���*��w��Z ��Ї|��@�Sq-bandit4@bandit:~/inhere$ cat ./-file05
W�cF���[Q
�
 ��a~���\0�ed(��ڨWbandit4@bandit:~/inhere$ cat ./-file06
?z=J"��oyvbandit4@bandit:~/inhere$ cat ./-file07
--------------------------------------
```
As you can see we found that the flag is in the `-file07` file.

However, I did not like my approach because what if there are thousands of files. With a little research I found that we can use `file` command to check the data type of the file. Now, combining `flag` command and `./*` will give us all the file names and their data type. `./*` stands for **all files in the current folder**, where `.` is current folder and `*` all files:
```bash
bandit4@bandit:~/inhere$ file ./*
./-file00: data
./-file01: OpenPGP Public Key
./-file02: OpenPGP Public Key
./-file03: data
./-file04: data
./-file05: data
./-file06: data
./-file07: ASCII text
./-file08: data
./-file09: data
```

Now all we need to is to use `cat ./"-file07"`:
```bash
bandit4@bandit:~/inhere$ cat ./"-file07"
-----------------------------
```

That is how we get the flag for bandit5!
