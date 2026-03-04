# Challenge Name: Unprotected admin functionality
# Platform: PortSwigger
# Difficulty: Apprentice

## 1. Vulnerability Type
Broken Access Control – Direct access to privileged functionality without authentication or role validation.
## 2. Root Cause
The application exposed the /administrator-panel endpoint without enforcing server-side authorization checks.
## 3. Attack Surface
`/administrator-panel`

## 4. Exploit Method
Visit `/robots.txt` -> Discover and navigate to `/administrator-panel` -> delete user `carlos`

## 5. Payload / Technique
No payload required.

## 6. Impact
* Unauthorized access to administrative panel

* Ability to delete arbitrary users

* Potential full privilege escalation
## 7. Reusable Pattern
When testing web applications:

* Always check /robots.txt and /sitemap.xml

* Perform directory brute-forcing (ffuf, dirsearch)

* Attempt direct access to hidden admin endpoints

* Never assume hidden paths are protected
## 8. Key Takeaway
All sensitive endpoints must enforce:

* Authentication

* Role-based authorization

* Server-side access control checks
