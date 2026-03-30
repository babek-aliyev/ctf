## 1. Vulnerability Type
DOM-based Cross-Site Scripting (DOM XSS)

## 2. Root Cause
User-controlled data from window.location.hash is inserted into a jQuery selector without sanitization, allowing selector injection and DOM XSS.

## 3. Attack Surface
/

## 4. Exploit Method
The application uses the following code:

$(window).on('hashchange', function(){
    var post = $('section.blog-list h2:contains(' + decodeURIComponent(window.location.hash.slice(1)) + ')');
    if (post) post.get(0).scrollIntoView();
});

Source:
window.location.hash

Sink:
jQuery selector (:contains())

The value of the URL fragment is inserted directly into a jQuery selector.

Because the input is not sanitized, an attacker can inject HTML that is interpreted by the browser, leading to JavaScript execution.

The code is only triggered on the hashchange event. Therefore, simply loading the page with a malicious hash does not execute the payload.

To exploit this, an iframe is used to first load the page without a hash, and then dynamically modify the URL to trigger the hashchange event.

## 5. Payload / Technique

<iframe src="https://LAB/#" onload="this.src+='<img src=1 onerror=print()>'" hidden></iframe>

The payload injects an <img> element with an onerror handler, which executes JavaScript when the image fails to load.

## 6. Impact
An attacker can execute arbitrary JavaScript in the victim’s browser without user interaction, potentially leading to session hijacking or phishing.

## 7. Reusable Pattern
Check whether user-controlled input is inserted into jQuery selectors, especially pseudo-selectors like :contains(), without sanitization.

## 8. Key Takeaway
User input must not be directly embedded into jQuery selectors, as it can lead to DOM-based XSS via selector injection.
