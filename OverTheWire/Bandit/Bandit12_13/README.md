# Bandit Level 12=> Level 13 | OverTheWire
## Description
The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work. Use mkdir with a hard to guess directory name. Or better, use the command “mktemp -d”. Then copy the datafile using cp, and rename it using mv (read the manpages!)

## Analysis
`data.txt` file a hexdump file and looks like this:
```bash
bandit12@bandit:~$ ls
data.txt
bandit12@bandit:~$ cat data.txt 
00000000: 1f8b 0808 2e17 ee68 0203 6461 7461 322e  .......h..data2.
00000010: 6269 6e00 0134 02cb fd42 5a68 3931 4159  bin..4...BZh91AY
00000020: 2653 59b6 7680 8b00 001a ffff fadd cfd6  &SY.v...........
00000030: f2e7 f6bb b87f 57ee fff3 b7d7 8bfd fafe  ......W.........
00000040: bffe fdfd d9ef 3dff bfff bdff b001 3aa1  ......=.......:.
00000050: a40d 007a 9901 a000 1a01 a000 1934 7a80  ...z.........4z.
00000060: 6993 469a 6800 0068 1a00 0340 680d 0d00  i.F.h..h...@h...
00000070: 01a6 8794 188d 0c27 a8d3 4608 8006 4d01  .......'..F...M.
00000080: 8800 3268 c8d0 3434 0006 9a19 0f50 3400  ..2h..44.....P4.
00000090: 1840 6403 2064 0034 1934 c468 c862 6868  .@d. d.4.4.h.bhh
000000a0: c801 a000 68f5 0e9e a346 8343 4346 8698  ....h....F.CCF..
000000b0: 40d0 0686 864c 9b48 0000 0003 40d3 4d34  @....L.H....@.M4
000000c0: 3231 3261 0003 46d4 01ea 0000 1a00 d000  212a..F.........
000000d0: 0d00 0020 c002 3067 df82 0e7a a6f5 b39a  ... ..0g...z....
000000e0: 6472 0263 7c59 8eaf c404 a738 aece fe35  dr.c|Y.....8...5
000000f0: 1921 a104 6114 268f 7f45 0411 a3de efc3  .!..a.&..E......
...
```
To start decompressing `data.txt` file we can use command `xxd` with flag `-r` to convert it to binary to check the compression type. However, in `/home/bandit12` folder we cannot create new files because of restrictions. That is why we need to do later operations in `/tmp/` folder. The reason behind it is `/tmp/` folder has permission `drwxrwxrwt`. `t` here indicates **sticky bit**, which allows anyone to create files. At the same time, it means other users can delete only their own files as a security feature.
## Solution
Therefore, we need to move to `/tmp/` folder and create a temporary working directory with either `mkdir` or `mktemp -d` commands:
```bash
bandit12@bandit:~$ cd /tmp/
bandit12@bandit:/tmp$ mktemp -d tempdirXXXX
tempdirOuNu
bandit12@bandit:/tmp$ cd tempdirOuNu
bandit12@bandit:/tmp/tempdirOuNu$ 
```
I used `mktemp -d` command here. `-d` flag stands for directory, and `XXXX` gets randomized to get unique name for directory.

Now we need to copy `data.txt` file from `/home/bandit12/` folder:
```bash
bandit12@bandit:/tmp/tempdirOuNu$ cp /home/bandit12/data.txt .
bandit12@bandit:/tmp/tempdirOuNu$ ls
data.txt
```
Let's try using `xxd` command again:
```bash
bandit12@bandit:/tmp/tempdirOuNu$ xxd -r data.txt > file.bin
bandit12@bandit:/tmp/tempdirOuNu$ ls
data.txt  file.bin
```
As you can see now it works! Then, we need to use command `file` to see the compression type and try to decompress the file:
```bash
bandit12@bandit:/tmp/tempdirOuNu$ file file.bin 
file.bin: gzip compressed data, was "data2.bin", last modified: Tue Oct 14 09:26:06 2025, max compression, from Unix, original size modulo 2^32 564
```

From now on, we will use command `file` and decompression commands to extract the data that we want. We do it multiple times because `data.txt` was compressed multiple times using different compression methods:
```bash
bandit12@bandit:/tmp/tempdirOuNu$ gunzip -c file.bin > data2.bin
bandit12@bandit:/tmp/tempdirOuNu$ ls
data2.bin  data.txt  file.bin
bandit12@bandit:/tmp/tempdirOuNu$ file data2.bin
data2.bin: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/tempdirOuNu$ bunzip2 data2.bin
bunzip2: Can't guess original name for data2.bin -- using data2.bin.out
bandit12@bandit:/tmp/tempdirOuNu$ ls
data2.bin.out  data.txt  file.bin
bandit12@bandit:/tmp/tempdirOuNu$ file data2.bin.out
data2.bin.out: gzip compressed data, was "data4.bin", last modified: Tue Oct 14 09:26:06 2025, max compression, from Unix, original size modulo 2^32 20480
bandit12@bandit:/tmp/tempdirOuNu$ gunzip -c data2.bin.out > data4.bin
bandit12@bandit:/tmp/tempdirOuNu$ ls
data2.bin.out  data4.bin  data.txt  file.bin
bandit12@bandit:/tmp/tempdirOuNu$ file data4.bin
data4.bin: POSIX tar archive (GNU)
bandit12@bandit:/tmp/tempdirOuNu$ tar -xf data4.bin
bandit12@bandit:/tmp/tempdirOuNu$ ls
data2.bin.out  data4.bin  data5.bin  data.txt  file.bin
bandit12@bandit:/tmp/tempdirOuNu$ file data5.bin
data5.bin: POSIX tar archive (GNU)
bandit12@bandit:/tmp/tempdirOuNu$ tar -xf data5.bin
bandit12@bandit:/tmp/tempdirOuNu$ ls
data2.bin.out  data4.bin  data5.bin  data6.bin  data.txt  file.bin
bandit12@bandit:/tmp/tempdirOuNu$ file data6.bin
data6.bin: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/tempdirOuNu$ bunzip2 data6.bin
bunzip2: Can't guess original name for data6.bin -- using data6.bin.out
bandit12@bandit:/tmp/tempdirOuNu$ ls
data2.bin.out  data4.bin  data5.bin  data6.bin.out  data.txt  file.bin
bandit12@bandit:/tmp/tempdirOuNu$ file data6.bin.out
data6.bin.out: POSIX tar archive (GNU)
bandit12@bandit:/tmp/tempdirOuNu$ tar -xf data6.bin.out
bandit12@bandit:/tmp/tempdirOuNu$ ls
data2.bin.out  data4.bin  data5.bin  data6.bin.out  data8.bin  data.txt  file.bin
bandit12@bandit:/tmp/tempdirOuNu$ file data8.bin
data8.bin: gzip compressed data, was "data9.bin", last modified: Tue Oct 14 09:26:06 2025, max compression, from Unix, original size modulo 2^32 49
bandit12@bandit:/tmp/tempdirOuNu$ gunzip -c data8.bin > data9.bin
bandit12@bandit:/tmp/tempdirOuNu$ ls
data2.bin.out  data4.bin  data5.bin  data6.bin.out  data8.bin  data9.bin  data.txt  file.bin
bandit12@bandit:/tmp/tempdirOuNu$ file data9.bin 
data9.bin: ASCII text
bandit12@bandit:/tmp/tempdirOuNu$ cat data9.bin 
The password is FO5dwFsc--------------------------
```
As you can see, we first determined the compression type and then decompressed it:
* `gunzip -c` => decompresses `gzip`, keeps original file unchaged and writes to standard output, that is why we used `> data2.txt`
* `bunzip2`=> simple command to decompress `bzip`
* `tar -xf` => decompresses **tar archive**. `-xf` flag extracts archive files of the given `tar` archive.

This is how we solve the current CTF! 
