# Challenge Name: DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded 
# Platform: PortSwigger
# Difficult: Practitioner

## 1. Vulnerability Type
DOM Cross-site scripting (XSS)

## 2. Root Cause
User input is interpreted as an AngularJS expression inside an ng-app context, leading to template injection.
## 3. Attack Surface
`/?search=`

## 4. Exploit Method
The application uses AngularJS with an ng-app directive, enabling expression evaluation. User input is reflected inside AngularJS templates, allowing template injection. To test for this, the payload `{{7*7}}` can be used. If the output is 49, the application is vulnerable.

## 5. Payload / Technique
`{{constructor.constructor('alert(1)')()}}

The payload uses AngularJS expression injection to access the Function constructor and execute arbitrary JavaScript.
## 6. Impact
Attacker can execute arbitrary javascript inside victim's browser that can lead to session hijacking, account takeover, or phishing.

## 7. Reusable Pattern
Check whether website uses deprecated framework with known vulnerabilities. If yes, try to escalate them.

## 8. Key Takeaway
Do not use deprecated frameworks that have known vulnerabilites such as AngularJS with its `ng-app` attribute directive. Moreover, always treat AngularJS expressions as executable code and avoid inserting user input into AngularJS templates without proper sanitization.


