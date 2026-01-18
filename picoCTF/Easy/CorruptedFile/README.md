# Corrupted File | picoCTF

In this CTF we are provided with corrupted file, from which we need to retrieve out flag.

## Analysis
Opening this file did not work because file is corrupted, os cannot recognize this file. I tried to use Cyberchef to get at least something. When I put this file into Cyberchef, I got an interesting output with JFIF at the top. With little research I found out that this JFIF is used for packaging JPEG-compressed image. That means our corrupted file probably is an image. I tried to run this file through online jpeg file restoring websites, but nothing succeeded. 


## Tools

I tried to use tools like **`xxd`** to view the details of this file. The output was not familiar to me. I copy pasted some part of the output in ChatGPT, and gave it everything I found so far. After suggesting it that this is a JFIF file, it explained me that the file header is started wrong.

Running `xxd` was giving me this output:
```bash
00000000: 5c78 ffe0 0010 4a46 4946 0001 0100 0001  \x....JFIF......
00000010: 0001 0000 ffdb 0043 0008 0606 0706 0508  .......C........
00000020: 0707 0709 0908 0a0c 140d 0c0b 0b0c 1912  ................
```

## Solution
Using tool called **`hexeditor`**, I changed the header part of this file to correct JFIF/JPEG header from **5c78** to **ffd8**:

```bash
00000000: ffd8 ffe0 0010 4a46 4946 0001 0100 0001  \x....JFIF......
00000010: 0001 0000 ffdb 0043 0008 0606 0706 0508  .......C........
00000020: 0707 0709 0908 0a0c 140d 0c0b 0b0c 1912  ................
```

## Flag
After changing header, our image got restored and contained the flag! We can both extract it using tesseract or just type it manually to picoCTF!!
