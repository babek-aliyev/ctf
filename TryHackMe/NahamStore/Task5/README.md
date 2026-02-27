# Nahamstore | Task 5 | TryHackMe
## Info
**Open redirect** is a vulnerability that trusts user's redirect location. That means hackers can modify the URI the of the original website, add stealthy redirect at the end to their malicious website. Open redirect makes phishing much easier because users see the original domain first and trusts the server without checking the rest of the URI. It looks something like this:
```bash
https://original.com/?redirect=https://evil.com
```
So when users see `www.original.com` they trust the link and press it and this link redirects them to malicious site that can steal their data, credentials, etc.
## Question 1
Find two URL parameters that produce an Open Redirect

### Solution
To find first redirect I used enumeration skills. I used `ffuf` to enumerate the original domain `http://nahamstore.thm/` to find if I can find some entry with code starting with '3'. Codes that start with '3' indicates to redirect. Below is the process of enumeration:
```bash
┌──(kali㉿kali)-[~]
└─$ ffuf -u http://nahamstore.thm/?FUZZ=https://www.google.com \
-w /usr/share/seclists/Discovery/Web-Content/raft-medium-words-lowercase.txt -t 50 -fc 200

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://nahamstore.thm/?FUZZ=https://www.google.com
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/Web-Content/raft-medium-words-lowercase.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 50
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response status: 200
________________________________________________

r                       [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 143ms]
:: Progress: [56293/56293] :: Job [1/1] :: 306 req/sec :: Duration: [0:02:27] :: Errors: 0 ::
```
Here we used `secList` wordlist to enumerate web contents of the web page. As you can see we set the redirect to `www.google.com` to check if redirect exists and filtered all 200 status codes because website accepts everything and it creates noise in our output. Later on I checked `http://nahamstore.thm/?r=https:www.google.com` and it redirected me to `google.com` page. So we found our first open redirect!

The **answer** for question 1 is: `r`

## Question 2
Find two URL parameters that produce an Open Redirect

### Solution
To find second open redirect I used manual approach. I was manually checking web app functionality to find redirects and found it. When we are not signed it, we can add items to basket. However, to proceed with the order we should be registered and logged in. So, after moving to `/basket` page, we should press either `login` or `register`. After pressing any of these links we see the following URI: `http://nahamstore.thm/register?redirect_url=/basket`. As you can see, the parameter shines that it is a redirect: `redirect_url`.To test this redirect for vulnerability I applied the same method here: modified it to `http://nahamstore.thm/register?redirect_url=https://www.google.com`. After changing the URI all we have to do is to finish the registration and upon finishing it we will be redirected to `www.google.com` page.

The **answer** for question 2 is: `redirect_url`
