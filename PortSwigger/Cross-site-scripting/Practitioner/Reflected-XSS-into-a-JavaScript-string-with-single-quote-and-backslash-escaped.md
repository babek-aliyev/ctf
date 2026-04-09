# Challenge Name: Reflected XSS into a JavaScript string with single quote and backslash escaped 
# Platform: PortSwigger
# Difficulty: Practitioner

## 1. Vulnerability Type
Reflected Cross-site Scripting

## 2. Root Cause
Web application does not escape dangerous characters such as `<` and `>`, that let attacker break out of html context.

## 3. Attack Surface
`/?search=`

## 4. Exploit Method
Web application uses the following script on client side:
```html
<script>
    var searchTerms = 'babek';
    document.write('<img src="/resources/images/tracker.gif?searchTerms='+encodeURIComponent(searchTerms)+'">');
</script>
```
By injecting `</script>`, the attacker breaks out of the existing script block at the HTML parsing level. This allows a new `<script>` tag to be introduced and executed.
## 5. Payload / Technique
```html
</script><script>alert(1)</script>
```
First `script` effectively breakes out of html context and closes first `script` tag. Afterwards, malicious `<script>alert(1)</script>` executes.

## 6. Impact
Attacker can execute arbitrary javascript code in victim's browser that can lead to session hijacking, account takeover, and phishing.

## 7. Reusable Pattern
Check whether all dangerous characters are escaped properly and whether user input is validated and sanitized.

## 8. Key Takeaway
Always validate and sanitize user input properly without leaving any security gaps.

