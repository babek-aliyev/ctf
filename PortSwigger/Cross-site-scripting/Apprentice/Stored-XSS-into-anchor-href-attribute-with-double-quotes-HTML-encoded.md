# Challenge Name: Stored XSS into anchor href attribute with double quotes HTML-encoded 
# Platform: PortSwigger
# Difficulty: Apprentice

## 1. Vulnerability Type
Stored Cross-Site Scripting (XSS)

## 2. Root Cause
User input is stored and later rendered inside an anchor tag's href attribute. Although double quotes are HTML-encoded, the application does not validate the URL scheme, allowing the use of the javascript: protocol.

## 3. Attack Surface
`/post?postId=`

## 4. Exploit Method
The application allows users to submit comments, including a website field.

The website value is later rendered inside an anchor tag's href attribute:
```html
<a href="USER_INPUT">username</a>
```
Although special characters like quotes are encoded, the input is still treated as a URL.

An attacker can supply a malicious URL using the javascript: scheme, such as:
```html
javascript:alert(1)
```
When a victim clicks the link, the JavaScript executes in their browser.

## 5. Payload / Technique
```html
javascript:alert(1)
```
## 6. Impact
Stored XSS allows an attacker to execute arbitrary JavaScript in a victim's browser, potentially leading to session hijacking, account takeover, or phishing attacks.

## 7. Reusable Pattern
Check whether user input is used inside href attributes and validate allowed URL schemes (e.g., http, https).

## 8. Key Takeaway
Never trust user input in href attributes. Always validate and restrict URL schemes to safe protocols like http and https.
