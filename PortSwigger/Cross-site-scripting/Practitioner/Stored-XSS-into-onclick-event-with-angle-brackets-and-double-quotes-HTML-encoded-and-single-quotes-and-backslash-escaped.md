# Challenge Name: Stored XSS into `onclick` event with angle brackets and double quotes HTML-encoded and single quotes and backslash escaped 
# Platform: PortSwigger
# Difficulty: Practitioner

## 1. Vulnerability Type
Stored Cross-site Scripting

## 2. Root Cause
The application reflects user input inside an onclick event handler and escapes certain characters, but fails to properly handle HTML-encoded equivalents such as `&apos;`, allowing injection into the JavaScript context.
## 3. Attack Surface
`post?postId=`

## 4. Exploit Method
Web application uses the following HTML code:
```html
<a id="author" href="https://babek.com" onclick="var tracker={track(){}};tracker.track('https://babek.com');">babek</a>
```
This application effectively escapes single quote, however, if single quote is written as `&apos;`, web application parses it without validating it, which leads to breaking out of context.
## 5. Payload / Technique
`http://babek?&apos;-alert(1)-&apos;`

This payload uses encoded single quotes to bypass filters of web application. We use `-alert(1)-`, that will execute `alert(1)` immediately and become `string-undefined-string` which is valid JS that returns `NaN`.
## 6. Impact
Attacker can execute arbitrary javascript cod inside victim's browser that can lead to session hijacking, account takeover, and phishing.

## 7. Reusable Pattern
Check whether encoded characters make web application behave differently, if yes, then it can be exploited.

## 8. Key Takeaway
Always escape dangerous characters and their encodings to prevent malicious inputs from attackers.

