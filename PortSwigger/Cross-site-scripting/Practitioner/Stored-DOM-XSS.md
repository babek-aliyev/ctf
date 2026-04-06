# Challenge Name: Stored DOM XSS 
# Platform: PortSwigger
# Difficulty: Practitioner

## 1. Vulnerability Type
DOM Cross-site Scripting

## 2. Root Cause
Web application uses `replace()` function to escape `<` and `>` characters. This method is vulnerable because `replace()` function only replaces first occurences allowing attacker to bypass this protection against XSS. 

## 3. Attack Surface
`/post?postId=`

## 4. Exploit Method
Web application uses the following code to protect itself against XSS:
```js
function escapeHTML(html) {
    return html.replace('<', '&lt;').replace('>', '&gt;');
}
```
Javascript `replace()` method replaces only first occurences, leaving security gap in the application. Attacker can bypass this security measure simply by adding `<>` sign in front of the payload.

## 5. Payload / Technique
`<><img src=/ onerror=alert(1)>`

Application encodes only first `<` and `>` leaving payload itself untouched. Therefore, XSS payload executes leading to stored XSS.

## 6. Impact
Attacker can run arbitrary javascript code in victim's browser that can lead to session hijacking, account takeover, or phishing.

## 7. Reusable Pattern
Check how web application encodes user input. If it uses vulnerable functions such as `replace()`, it can be bypassed and exploited.

## 8. Key Takeaway
Do not use vulnerable functions like `replace()` to protect web application from XSS. Instead of blocking first occurences, it is better idea to use regex to block users from parsing malicious characters like `<>`.


