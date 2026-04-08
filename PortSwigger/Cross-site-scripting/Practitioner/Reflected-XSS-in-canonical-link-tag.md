# Challenge Name: Reflected XSS in canonical link 
# Platform: PortSwigger
# Difficulty: Practitioner

## 1. Vulnerability Type
Reflected Cross-site Scripting

## 2. Root Cause
Web application uses user input in its canonical link `href` attribute without proper validation, that leaves security gap.

## 3. Attack Surface
Home page

## 4. Exploit Method
Web application has two security gaps: it parse user input directly into `hfef` attribute inside canonical link and uses blacklisting to block double quotes `"` to prevent breaking out of attribute (`href` in this case). However, web application does not parse all special characters into `href` the same way. In this web application, if user uses single quote `'`, web application tries to fix html from breaking and therefore parses single quote as double quote and allows attacker to break out of `href` attribute. After that, attacker can use new attributes and exploit XSS injection.

## 5. Payload / Technique
`/?'accesskey='x'onclick='alert(1)`
In this payload, we do not use space, at it is parsed in encoded form and breaks payload. We add `accesskey='x'` because we are given that victim will use combination of `ALT+X`, `CTRL+ALT+X`, `ALT+SHIFT+X`. `onclick` will execute the `alert(1)` function when victim uses shorcut. We wrote single quote before `alert(1)` to close the trailing double quote from `href`.
## 6. Impact
Attacker can run arbitrary javascript code in victim's browser, that can lead to session hijacking, account takeover, phishing.

## 7. Reusable Pattern
Check if user input appears in any html tag, attribute and whether it is validated properly or not.

## 8. Key Takeaway
Always be cautious where you parse user's input and always validate it to prevent vulnerabilites like cross-site scripting.


