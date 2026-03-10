# Challenge Name: Unprotected admin functionality with unpredictable URL
# Platform: PortSwigger
# Difficulty: Apprentice

## 1. Vulnerability Type
Broken Access Control – Sensitive endpoint accessible without proper authorization checks.
## 2. Root Cause
The application relied on client-side logic (isAdmin JavaScript variable) to control visibility of the admin panel link.

However:

* The admin endpoint /admin-snqvol existed server-side.

* No server-side authorization check was enforced.

* Access control was implemented only in frontend JavaScript.

Client-side controls can be bypassed easily by directly accessing the endpoint.
## 3. Attack Surface
`/admin-snqvol`

## 4. Exploit Method
1) Inspect page 
2) Read:
```js
var isAdmin = false;
if (isAdmin) {
   var topLinksTag = document.getElementsByClassName("top-links")[0];
   var adminPanelTag = document.createElement('a');
   adminPanelTag.setAttribute('href', '/admin-snqvol');
   adminPanelTag.innerText = 'Admin panel';
   topLinksTag.append(adminPanelTag);
   var pTag = document.createElement('p');
   pTag.innerText = '|';
   topLinksTag.appendChild(pTag);
}
```
3) Observed that admin panel link is conditionally rendered in the client-side UI.
4) Manually navigated to `/admin-snqvol`
5) Gained unauthorized access to admin panel and deleted user `carlos`.
## 5. Payload / Technique
No payload required.

## 6. Impact
Unauthorized access to admin privileged endpoints. Access to admin `delete` function. Potentially fully-privileged access.

## 7. Reusable Pattern
Inspect page source and JavaScript files to identify hidden or conditionally rendered privileged endpoints. Attempt direct access to those endpoints.
## 8. Key Takeaway
Always authorize, protect, and validate sensitive endpoints on server-side. Do not rely on client-side conditions. 
