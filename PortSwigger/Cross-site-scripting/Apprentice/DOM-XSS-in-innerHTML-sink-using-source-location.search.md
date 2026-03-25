# Challenge Name: DOM XSS in `innerHTML` sink using source `location.search`
# Platform: PortSwigger
# Difficulty: Apprentice

## 1. Vulnerability Type
DOM Cross-Site Scripting

## 2. Root Cause
The application reads user-controlled data from `location.search` and writes it to the page using `innerHTML` without sanitization.

Because the data flows from a controllable source to a dangerous sink, it allows execution of arbitrary JavaScript in the browser.

## 3. Attack Surface
`/?search=`

## 4. Exploit Method
Web application uses the following script code for its search function:
```js
<script>
    function doSearchQuery(query) {
        document.getElementById('searchMessage').innerHTML = query;
    }
    var query = (new URLSearchParams(window.location.search)).get('search');
    if(query) {
        doSearchQuery(query);
    }
</script>
```
It does not sanitize user input which leads to DOM XSS injection.

Source:
window.location.search → user-controlled input

Sink:
innerHTML

The value of the search parameter is inserted directly into HTML without sanitization.

By injecting characters that break the HTML attribute, it is possible to inject a script tag and execute JavaScript.

## 5. Payload / Technique
`<img src=/ onerror=alert("XSS")>`

## 6. Impact
Using DOM XSS injection attacker can obtain session hijacking, account takeover, phishing, malicious redirects, etc.

## 7. Reusable Pattern
Check source codes for functions in the web application: if they use dangerous methods like parsing `window.location.search` without sanitizing, this can be potentially exploited.

## 8. Key Takeaway
Never write user-controlled data directly into the DOM using unsafe sinks such as innerHTML.
Always sanitize input or use safe DOM APIs.



