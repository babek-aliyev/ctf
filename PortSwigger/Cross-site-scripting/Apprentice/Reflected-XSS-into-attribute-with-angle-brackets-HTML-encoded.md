# Challenge Name: Reflected XSS into attribute with angle brackets HTML-encoded 
# Platform: PortSwigger
# Difficulty: Apprentice

## 1. Vulnerability Type
Reflected Cross-Site Scripting (XSS)

## 2. Root Cause
User input is reflected inside an HTML attribute where angle brackets are encoded, but quotation marks are not properly handled, allowing attribute injection.

## 3. Attack Surface
`/?search=`

## 4. Exploit Method
The application reflects user input inside an input field’s value attribute:
```html
<input value="USER_INPUT">
```
Although angle brackets (< >) are encoded, quotation marks are not.

An attacker can break out of the value attribute and inject a new HTML attribute with an event handler.

## 5. Payload / Technique
```html
" onmouseover=alert(1) x="
```
This payload:
- closes the existing attribute
- injects a new attribute (onmouseover)
- executes JavaScript when the user interacts with the element

## 6. Impact
Reflected XSS can allow an attacker to execute arbitrary JavaScript in the victim’s browser, potentially leading to session hijacking or account takeover.

## 7. Reusable Pattern
Check whether user input is reflected inside HTML attributes and whether quotes are properly encoded.

## 8. Key Takeaway
Proper output encoding must be context-aware. Encoding angle brackets alone is not sufficient when input is placed inside HTML attributes.
