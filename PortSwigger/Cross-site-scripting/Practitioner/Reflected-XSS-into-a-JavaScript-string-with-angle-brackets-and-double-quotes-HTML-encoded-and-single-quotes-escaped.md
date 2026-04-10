# Challenge Name: Reflected XSS into a JavaScript string with angle brackets and double quotes HTML-encoded and single quotes escaped 
# Platform: PortSwigger
# Difficulty: Practitioner

## 1. Vulnerability Type
Reflected Cross-site Scripting

## 2. Root Cause
Web application does not escape backslash properly, which leads to breaking out of javascript context.

## 3. Attack Surface
`/?search=`

## 4. Exploit Method
Web application uses the following script code:
```html
<script>
    var searchTerms = '\\'; alert(1); //';
    document.write('<img src="/resources/images/tracker.gif?searchTerms='+encodeURIComponent(searchTerms)+'">');
</script>
```
Web applications escapes single quotes using backslash. However, the backslash itself is not properly escaped, therefore, when is inserted in combination with single quote, user's backslash effectively escapes backslash that escapes single quote, leading to breaking out of javascript context.

## 5. Payload / Technique
`\'; alert(1); //`

The backslash in payload escapes the backslash of single quote and leads to escaping from string. Later, malicious function is executed, and the rest of code is commented to prevent errors.

## 6. Impact
Attacker can run arbitrary javascript code inside victim's browser that can lead to session hijacking, account takeover, and phishing.

## 7. Reusable Pattern
Always check whether all special characters are escaped or encoded properly. If not, this will create exploitable security gap in application.

## 8. Key Takeaway
Always escape and encode special characters like `'`,`"`,`\`,`<>`, and etc. that can be dangerous for application security.

