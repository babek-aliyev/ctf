# PIE Time | picoCTF

We have vuln.c code which shows the logic behind the running instance, to which we need to connect using netcat. Then, we need to find the address of win() function to retrieve the flag.

## What We Have
After running

```bash
nc rescued-float.picoctf.net 65257
```
We get output:
```bash
Address of main: 0x5576643b333d
Enter the address to jump to, ex => 0x12345:
```

## Analysis

To analyze the binary `vuln` file, we need to use tool called **`nm`**. This tool will show use global variables, functions and their addresses. However, it shows their addresses using offsets, as `vuln` file is ASLR (Address Space Layout Randomization) and PIE (Position Independent Executable). Basically, the last 12 bits (3 bytes) are showing offset in this particular binary file. For example, when we run `nm`, we get something like this:
```bash
000000000000133d T main
                 U printf@@GLIBC_2.2.5
                 U putchar@@GLIBC_2.2.5
                 U puts@@GLIBC_2.2.5
0000000000001200 t register_tm_clones
0000000000001289 T segfault_handler
                 U setvbuf@@GLIBC_2.2.5
                 U signal@@GLIBC_2.2.5
                 U __stack_chk_fail@@GLIBC_2.4
00000000000011a0 T _start
0000000000004010 B stdout@@GLIBC_2.2.5
0000000000004010 D __TMC_END__
00000000000012a7 T win
```

## Answer

That means we know the offsets of all functions in current binary file, so if main function is at 0x...33d, then win() function will be at 0x...2a7. That address reads as flag.txt and retrieves ctf!
