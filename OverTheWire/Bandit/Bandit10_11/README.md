# Bandit Level 10=> Level 11 | OverTheWire
## Description
The password for the next level is stored in the file data.txt, which contains base64 encoded data

## Analysis
This is the output we get when we try to read encoded `data.txt`:
```bash
bandit10@bandit:~$ cat data.txt 
VGhlIHBhc3N3b3JkIGlzIGR0UjE3M2ZaS2IwUlJzREZTR3NnMlJXbnBOVmozcVJyCg==
```
`data.txt` is **base64** encoded string, which contains the password for the next level. We can decode this file using several methods:
1) We can use website called Cyberchef
2) Or even simpler, we can use command `base64` in terminal to decode the `data.txt`

## Solution

The `base64` command on its own **encodes** file into base64 format. However, if we add `-d` flag, then it **decodes** it. We can always check for flags using `--help` command:
```bash
bandit10@bandit:~$ base64 --help
Usage: base64 [OPTION]... [FILE]
Base64 encode or decode FILE, or standard input, to standard output.

With no FILE, or when FILE is -, read standard input.

Mandatory arguments to long options are mandatory for short options too.
  -d, --decode          decode data
  -i, --ignore-garbage  when decoding, ignore non-alphabet characters
  -w, --wrap=COLS       wrap encoded lines after COLS character (default 76).
                          Use 0 to disable line wrapping
      --help        display this help and exit
      --version     output version information and exit

The data are encoded as described for the base64 alphabet in RFC 4648.
When decoding, the input may contain newlines in addition to the bytes of
the formal base64 alphabet.  Use --ignore-garbage to attempt to recover
from any other non-alphabet bytes in the encoded stream.

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Full documentation <https://www.gnu.org/software/coreutils/base64>
or available locally via: info '(coreutils) base64 invocation'
```
## Answer
`base64 -d data.txt` command gives us decoded string:
```bash
bandit10@bandit:~$ base64 -d data.txt 
The password is dtR173f--------------------------
```
