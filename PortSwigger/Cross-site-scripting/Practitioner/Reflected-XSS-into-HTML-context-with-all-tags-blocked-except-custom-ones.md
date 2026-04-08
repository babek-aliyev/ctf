# Challenge Name:  Reflected XSS into HTML context with all tags blocked except custom ones
# Platform: PortSwigger
# Difficulty: Practitioner

## 1. Vulnerability Type
Reflected Cross-site Scripting

## 2. Root Cause
Web application uses WAF (Web Application Firewall) to protect against common XSS injections. However, WAF does not filter custom tags with attributes which leads to security gap.

## 3. Attack Surface
`/?search=`

## 4. Exploit Method
Simple payload like `<img src=/ onerror=print()>` does not work, because WAF filters the `<img>` tag. It returns error saying tag is not allowed. That error helps attacker to enumerate list of allowed tags. After copying list of all tags from PortSwigger XSS cheat-sheet, it is possible to enumerate list of tags that are allowed. By doing so attacker can detect that custom `<custom-tag>` tag is not filtered. Next step is craft a payload that will auto-execute. This can be done by `onfocus` attribute. To make it auto-executable, adding `id`, `tabindex` and anchor (#) in the URL will be enough.

Note:
I also tried to use `<body oncontentvisibilityautostatechange=print() style=display:block;content-visibility:auto>` which does not even require exploit server and auto-executes in victim's browser. I tested it both Chrome and Firefox making sure they both work. However, it was not accepted by PortSwigger lab I don't know why.
## 5. Payload / Technique
```html
<script>
    location = "URL-of-lab/?search=URL-encoded(<custom-tag id="babek" onfocus=alert(document.cookie) tabindex=1>)#babek
```
We add this payload to the body of response in our exploit server. We are making `custom-tag` focusable using `tabindex`, and then when loading the page, we are trying to go for `babek` section using anchor #. `location` is built in javascript and redirects the page to given URL.
Mine:
`<body oncontentvisibilityautostatechange=print() style=display:block;content-visibility:auto>"` -> works without exploit server without user interaction.
## 6. Impact
Attacker can run arbitrary javascript in victim's browser that can lead to account takeover, session hijacking, and phishing.

## 7. Reusable Pattern
Check if security measurements such as WAF filter all tags, attributes, etc. Also check if error reveal too much information that can lead to enumeration.

## 8. Key Takeaway
Do not reveal too much information on errors that can lead to enumeration. Try to filter all dangerous tags (even custom ones) and filters using technologies like WAF.
