# Bandit Level 13=> Level 14 | OverTheWire
# Description
The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Look at the commands that logged you into previous bandit levels, and find out how to use the key for this level.
# Analysis
After connecting to user `bandit13`, we observe the following files on command `ls`:
```bash
bandit13@bandit:~$ ls
HINT  sshkey.private
```
Important file here is `sshkey.private`, that contains private SSH key that can be used to log into `bandit14` machine.
# Solution
We can read that `sshkey.private` SSH private key and copy it:
```bash
bandit13@bandit:~$ cat sshkey.private 
-----BEGIN RSA PRIVATE KEY-----
...
-----END RSA PRIVATE KEY-----
```
After copying this private SSH key, we should exit `bandit13` machine, create new `sshkey.txt` file on our own machine and parse that copied private key there. Then we should set correct permissions so SSH will not refuse and log into the `bandit14` machine using the following commands:
```bash
bandit13@bandit:~$ exit
logout
Connection to bandit.labs.overthewire.org closed.
                                                                                                                    
┌──(kali㉿kali)-[~]
└─$ vim ss.txt 
                                                                                                                    
┌──(kali㉿kali)-[~]
└─$ chmod 600 ss.txt              
                                                                                                                    
┌──(kali㉿kali)-[~]
└─$ ssh -i ss.txt bandit14@bandit.labs.overthewire.org -p 2220
```

After successfully connecting to `bandit14` machine, we can find the password inside `/etc/bandit_pass/bandit14` file. This is how we get the password for `bandit14`!.
