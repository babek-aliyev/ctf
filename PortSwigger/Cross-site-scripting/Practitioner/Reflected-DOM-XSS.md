# Challenge Name: Reflected DOM XSS 
# Platform: PortSwigger
# Difficulty: Practitioner

## 1. Vulnerability Type
DOM Cross-site Scripting

## 2. Root Cause
Web application has two vulnerabilities: 1) it uses `eval()` to assign javascript code to variable, 2) it uses blacklisting - even though it escapes double quotes, backslash is not escaped, that can lead to break out of string.

## 3. Attack Surface
`/?search=`

## 4. Exploit Method
Web application uses the following code:
```js
var xhr = new XMLHttpRequest();
xhr.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        eval('var searchResultsObj = ' + this.responseText);
        displaySearchResults(searchResultsObj);
    }
};
...
```
It takes response text and uses it inside dangerous method `eval()`. The response text depends on user input, that can lead to potential DOM XSS. After intercepting requests and responses we can see that we get the following response after typing `XSS` in the search:
```bash
{"results":[],"searchTerm":"XSS"}
```
Using this information, it is possible to break out of the string. To do so,it is needed to use `\` (backslash) before double quotes, because they are escaped by web app.
## 5. Payload / Technique
`\"/alert(1)}//`

This payload successfully cancels out double quote escape with backslash. `/` is used to separate first part with second: when response retuns the data, `alert(1)` will be executed instantly and become `undefined`. String / undefined = string / NaN => NaN. This is a valid javascript code and does not return syntax error. The two `//` in the end successfully comments out everything after it.
## 6. Impact
Attacker can run arbitrary javascript code in victim's browser, that can lead to session hijacking, account takeover, or phishing.

## 7. Reusable Pattern
Check whether web application uses dangerous methods like `eval()`: if yes, check if it accepts user input. If this is also yes, try to exploit it.

## 8. Key Takeaway
Do not use dangerous methods like `eval()` and always use whitelisting to prevent dangerous vulnerabilities such as DOM XSS.


