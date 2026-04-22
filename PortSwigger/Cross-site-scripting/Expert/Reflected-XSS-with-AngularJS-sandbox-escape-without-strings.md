# Challenge Name: Reflected XSS with AngularJS sandbox escape without strings 
# Platform: PortSwigger
# Difficulty: Expert

## 1. Vulnerability Type
Reflected Cross-site Scripting

## 2. Root Cause
Web application uses older version of AngularJS that contains security sandbox. This sandbox gives false sense of security and can be exploited.

## 3. Attack Surface
`/?search=x`

## 4. Exploit Method
To escape this AngularJS sandbox, attacker can use the payload crafted by Gareth Heyes. His payload uses `toString().constructor` to access Function constructor through String constructor. Then he overwrites the `charAt` function using `prototype` of String function. We do this because AngularJS sandbox restricts how strings behave, therefore, overwriting `charAt` breaks Angular's assumptions and weakens the protection. Later on, this payload has obfuscated code that orders the given array by executing `fromCharCode` function for each item in the array. Notice that overwriting the charAt function is necessary to break AngularJS sandbox protections. The sandbox relies on certain string behaviors, and modifying charAt disrupts these assumptions, allowing the malicious expression to execute. The fromCharCode function itself is not restricted, but without bypassing the sandbox, the payload would not execute successfully.
## 5. Payload / Technique
`/?search=babek&toString().constructor.prototype.charAt%3d[].join;[1]|orderBy:toString().constructor.fromCharCode(120,61,97,108,101,114,116,40,49,41)=babek`

We used `fromCharCode(120,61,97,108,101,114,116,40,49,41)` because lab said strings are not allowed.
## 6. Impact
Attacker can run arbitrary javascript code inside victim's browser that can lead to account takeover, session hijacking, and phishing.

## 7. Reusable Pattern
Check whether application uses older version of AngularJS by trying famous sandbox escape payloads.

## 8. Key Takeaway
Use newer version of AngularJS that is not prone to sandbox escape. Avoid injecting user input into Angular expressions.


