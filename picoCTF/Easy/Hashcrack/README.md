# Hashcrack | picoCTF

This CTF launches an instance to which we need to connect using netcat. After connecting to this instance we start the exploitation. 

## Process
I used website called CrackStation ( https://crackstation.net/ )  to find the hashed passwords. It has the most popular and used passwords and their hashes. This technique is called *Rainbow Table Attack*.

After connecting to the instance and entering the input for the provided hashes, we get the following outputs:

```bash
┌──(kali㉿kali)-[~]
└─$ nc verbal-sleep.picoctf.net 56426
Welcome!! Looking For the Secret?

We have identified a hash: 482c811da5d5b4bc6d497ffa98491e38
Enter the password for identified hash: ***************
Correct! You've cracked the MD5 hash with no secret found!

Flag is yet to be revealed!! Crack this hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
Enter the password for the identified hash: **************
Correct! You've cracked the SHA-1 hash with no secret found!

Almost there!! Crack this hash: 916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745
Enter the password for the identified hash: **************
Correct! You've cracked the SHA-256 hash with a secret found. 
The flag is: picoCTF{**************}
```

## Answer
And this is how we get the flag for this CTF.

It is always good to check **Rainbow Table** for existing hashes, as it will increase the speed of exploitation a lot. 
