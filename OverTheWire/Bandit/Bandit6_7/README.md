# Bandit Level 6=> Level 7 | OverTheWire
## Description
The password for the next level is stored somewhere on the server and has all of the following properties:
* owned by user bandit7
* owned by group bandit6
* 33 bytes in size

## Analysis
This CTF challenge looks like the previous one: we need to find a file containing flag stored somewhere on the server. First we need to check what folder do we have in bandit6 folder:
```bash
bandit6@bandit:~$ ls
bandit6@bandit:~$ 
```
As you can see we have nothing interesting here. Even if we try to see the hidden files and folders, we still get pretty much nothing:
```bash
bandit6@bandit:~$ ls -a
.  ..  .bash_logout  .bashrc  .profile
bandit6@bandit:~$ 
```
## Solution
At this point, we know we have nothing inside bandit6, so we need to change the directory to root directory. We can do it by using command `cd ..`:
```bash
bandit6@bandit:~$ cd ..
bandit6@bandit:/home$ ls
bandit0   bandit2       bandit29      bandit7    drifter0   drifter7     krypton4    manpage0  maze4    narnia6  utumno7   vortex18  vortex6
bandit1   bandit20      bandit29-git  bandit8    drifter1   drifter8     krypton5    manpage1  maze5    narnia7  utumno8   vortex19  vortex7
bandit10  bandit21      bandit3       bandit9    drifter10  drifter9     krypton6    manpage2  maze6    narnia8  vortex0   vortex2   vortex8
bandit11  bandit22      bandit30      behemoth0  drifter12  formulaone0  krypton7    manpage3  maze7    narnia9  vortex1   vortex20  vortex9
bandit12  bandit23      bandit30-git  behemoth1  drifter13  formulaone1  leviathan0  manpage4  maze8    ubuntu   vortex10  vortex21
bandit13  bandit24      bandit31      behemoth2  drifter14  formulaone2  leviathan1  manpage5  maze9    utumno0  vortex11  vortex22
bandit14  bandit25      bandit31-git  behemoth3  drifter15  formulaone3  leviathan2  manpage6  narnia0  utumno1  vortex12  vortex23
bandit15  bandit26      bandit32      behemoth4  drifter2   formulaone5  leviathan3  manpage7  narnia1  utumno2  vortex13  vortex24
bandit16  bandit27      bandit33      behemoth5  drifter3   formulaone6  leviathan4  maze0     narnia2  utumno3  vortex14  vortex25
bandit17  bandit27-git  bandit4       behemoth6  drifter4   krypton1     leviathan5  maze1     narnia3  utumno4  vortex15  vortex3
bandit18  bandit28      bandit5       behemoth7  drifter5   krypton2     leviathan6  maze2     narnia4  utumno5  vortex16  vortex4
bandit19  bandit28-git  bandit6       behemoth8  drifter6   krypton3     leviathan7  maze3     narnia5  utumno6  vortex17  vortex5
```
This folder does not give us any useful information as it just contains other levels of CTF, and we cannot access any of them because of restrictions. So we need to change the directory again using `cd ..`:
```bash
bandit6@bandit:/home$ cd ..
bandit6@bandit:/$ ls
behemoth           boot     etc         krypton  lib64              lost+found  media   opt   run                 snap  tmp     var
bin                dev      formulaone  lib      lib.usr-is-merged  manpage     mnt     proc  sbin                srv   usr     vortex
bin.usr-is-merged  drifter  home        lib32    libx32             maze        narnia  root  sbin.usr-is-merged  sys   utumno
```
Now we are inside the system files of this server. What we can use now is the combination of `find` command with flags that will specify the output for us.

Here below is the command I used for this purpose:
```bash
bandit6@bandit:/$ find . -maxdepth 7 -type f -group bandit6 -user bandit7 -size 33c 2>/dev/null 
```
Here:
* `find .` => searches current directory
* `-maxdepth 7` => sets the maximum depths of subfolder to 7. I chose it arbitrary to be sure to cover most of folders. It is better to use more because there is a chance to miss the file due to depth limit
* `-type f` => searches for files only
* `-group bandit6` => searches for files owned by group **"bandit6"** 
* `-user bandit7` => similarly, searches for files owned by user **bandit7**
* `-size 33c` => flag for files with size of 33 bytes. Byte is indicated as 'c'
* `2>/dev/null` => ignores the error messages as we can get lots of **"Permission denied"** errors during this search

Now, after running this command, we get the following output:
```bash
bandit6@bandit:/$ find . -maxdepth 7 -type f -group bandit6 -user bandit7 -size 33c 2>/dev/null 
./var/lib/dpkg/info/bandit7.password
bandit6@bandit:/$ 
```
## Answer
All we have to do is to run the `cat` command to read the password for bandit7:
```bash
bandit6@bandit:/$ cat ./var/lib/dpkg/info/bandit7.password
morbNTD---------------------
bandit6@bandit:/$ 
```

