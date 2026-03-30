# Challenge Name: Reflected XSS into a JavaScript string with angle brackets HTML encoded 
# Platform: PortSwigger
# Difficulty: Apprentice

## 1. Vulnerability Type
Reflected XSS (Cross-site Scripting)

## 2. Root Cause
User input is reflected inside a JavaScript string context, and special characters like single quotes are not escaped, allowing breaking out of the string and injecting arbitrary JavaScript.
## 3. Attack Surface
`/?search=`

## 4. Exploit Method
Web application uses the following code script for search query:
```js
<script>
    var searchTerms = ''; alert(1) ; x='god';
    document.write('<img src="/resources/images/tracker.gif?searchTerms='+encodeURIComponent(searchTerms)+'">');
</script>
```
As you can see, even though angle brackets are encoded, by using single quote attacker can perform javascript string injection. For example, using single quote in the start of the string will close the `seachTerms` variable and the rest of the string will be implemented as javascript code.
## 5. Payload / Technique
```js
'; alert(1) ; x='good
```
In this payload, first single quote ends `searchTerms` variable and the following semicolon (;) ends line, after that `alert(1)` is interpreted as a new line entry and is executed. I added the last `x='good` to avoid error in syntax.
## 6. Impact
Attacker can execute arbitrary javascript in user's browser, that can lead to session hijacking, account takeover, or phishing.

## 7. Reusable Pattern
Check if user input is sanitized and validated before being processed, if not that can lead to potential reflected or stored xss.

## 8. Key Takeaway
Always validate and sanitize user input before parsing it into html, script code. This will prevent cross-site scripting injections.


