# EVEN RSA CAN BE BROKEN ??? | picoCTF
In this CTF we are given three numbers: N,e, and ciphertext after connecting to the launcher using netcat. Our purpose is to decrypt RSA and find the flag. We are also given a python code to help us visualize how RSA encryption is done.

## Analysis
First of all, I checked the python code to understand the algorithm how RSA encryption works. At first it was very hard to understand, but later with additional research I finally understood it. So the main problem in this CTF was that we did not know the prime numbers p and q to decrypt this RSA encryption. I was not really sure what to do, so I tried to use the hints provided by picoCTF. The hints pointed to N and asked about anything interesting about N. That was the moment of truth. I noticed that all N values provided by instance are even numbers; however, we know that `N = p * q`, where *p* and *q* are odd numbers. That means the N also should have been an odd number. 

## Solution
So, there is only one conclusion: if N is even, that means either p or q is 2. After finding out one prime, RSA encryption becomes very weak and easily solvable. I researched and wrote a python code, which decrypts the RSA encryption:
```python
from Crypto.Util.number import long_to_bytes, inverse

# Given values
N = 18050914195872353262907827116669494887829882395077363796802093354707010685600084901997191977598948238444805346883059845257910489595133559465140879768662118
e = 65537
c = 9362530038544990893457717886274375070699002272210513108226678525227068709737083508543502818039078548566103969495062727635622044069094688059400402295290655

# Factor N
p = 2
q = N // 2

# Compute phi(N)
phi = (p - 1) * (q - 1)

# Compute private key exponent
d = inverse(e, phi)

# Decrypt ciphertext
m = pow(c, d, N)
flag = long_to_bytes(m)

print("Flag:", flag.decode())

```
Using the found information, we found the solution for current CTF!
