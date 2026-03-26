# Challenge Name: DOM XSS in jQuery anchor `href` attribute sink using `location.search` source 
# Platform: PortSwigger
# Difficulty: Apprentice

## 1. Vulnerability Type
DOM Cross-Site Scripting (DOM XSS) 

## 2. Root Cause
Web application blindly trusts user input in URI and adds it to "Back" button's reference, which leads to DOM XSS.

## 3. Attack Surface
`feedback?returnPath=`

## 4. Exploit Method
Web application uses the following code snippet:
```js
<div class="is-linkback">
     <a id="backLink">Back</a>
</div>
<script>
    $(function() {
        $('#backLink').attr("href", (new URLSearchParams(window.location.search)).get('returnPath'));
    });
</script>
```
Here as `href` attribute of `<a>` acts as a sink and `window.location.search` acts as a search. Search does not verify or sanitize user input that leads to DOM XSS.

## 5. Payload / Technique
```js
javascript:alert(document.cookie)
```

## 6. Impact
DOM cross-site scripting can lead to account takeover, exposed credentials, cookie values, etc.

## 7. Reusable Pattern
Always check if web applications uses dangerous methods like `href` without sanitizing user input.

## 8. Key Takeaway
Never trust user input without validation and sanitizing.


