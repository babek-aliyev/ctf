# Challenge Name: Reflected XSS into a template literal with angle brackets, single, double quotes, backslash and backticks Unicode-escaped 
# Platform: PortSwigger
# Difficulty: Practitioner

## 1. Vulnerability Type
Reflected Cross-site Scripting

## 2. Root Cause
Web application does not escape or encode `$` and `{}` that can be used to exploit cross-site scripting.

## 3. Attack Surface
`/?search=`

## 4. Exploit Method
Web application uses the following code:
```html
<h1 id="searchMessage">0 search results for 'undefined'</h1>
<script>
    var message = `0 search results for '${alert(1)}'`;
    document.getElementById('searchMessage').innerText = message;
</script>
```
In JavaScript template literals, expressions inside ${...} are evaluated at runtime. By injecting ${alert(1)}, the attacker forces execution of arbitrary JavaScript when the template literal is processed.

## 5. Payload / Technique
`${alert(1)}`

## 6. Impact
Attacker can run arbitrary javascript code in victim's browser that can lead to session hijacking, account takeover, phishing.

## 7. Reusable Pattern
Check if all dangerous characters are escaped. If not, there might be chance to exploit the application.

## 8. Key Takeaway
Always validate, escape and encode all dangerous characters that can leave security gap in web application.


