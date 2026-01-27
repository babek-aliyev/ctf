# Bandit Level 2=>Level 3 | OverTheWire

## Description
The password for the next level is stored in a hidden file in the inhere directory.
## Analysis
Hidden file almost always means using command `ls` with flag `-a` which shows hidden files in the current folder.
## Solution
First we need to check what files/directories we have in the current `bandit` level. We can check it using the command `ls`:
```bash
bandit3@bandit:~$ ls
inhere
```
As it says in the description, we have `inhere` folder, which should contain our hidded flag file.
## Answer`
Now, inside `inhere` folder, all we have to do is run the following command:
```bash
bandit3@bandit:~/inhere$ ls
bandit3@bandit:~/inhere$ ls -a
.  ..  ...Hiding-From-You
```
As you can see, without flag `-a` we cannot see the hidden flag in this directory. But later after using `-a` reveals the hidden file.

Now all we have to do is read the hidden file:
```bash 
bandit3@bandit:~/inhere$ cat "...Hiding-From-You"
---------------------------------
```

That is how we get the flag for bandit4!

