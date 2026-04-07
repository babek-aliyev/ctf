# Challenge Name:  Reflected XSS into HTML context with most tags and attributes blocked
# Platform: PortSwigger
# Difficulty: Practitioner

## 1. Vulnerability Type
Reflected Cross-site Scripting

## 2. Root Cause
Web application uses WAF (Web Application Firewall) to protect against common XSS injections. However, WAF does not filter all tags and attributes which leads to security gap.

## 3. Attack Surface
`/?search=`

## 4. Exploit Method
Simple payload like `<img src=/ onerror=print()>` does not work, because WAF filters the `<img>` tag. It returns error saying tag is not allowed. That error helps attacker to enumerate list of allowed tags. After copying list of all tags from PortSwigger XSS cheat-sheet, it is possible to enumerate list of tags that are allowed. By doing so attacker can detect that `<body>` tag is not filtered. Next step is enumerating list of allowed attributes, because WAF filters attributes too. Its error message is different which helps attacker to enumerate. After enumeration attacker find out list of attributes that bypass filter. These are `onresize`, `oncontentvisibilityautostatechange`, etc. In this particular lab, we should use `onresize` attribute in exploit server with `<iframe>`. To make payload execute without user interaction attacker add `onload=this.style.width='100px'` inside `iframe` tag.

Note:
I also tried to use `<body oncontentvisibilityautostatechange=print() style=display:block;content-visibility:auto>` which does not even require exploit server and auto-executes in victim's browser. I tested it both Chrome and Firefox making sure they both work. However, it was not accepted by PortSwigger lab I don't know why.
## 5. Payload / Technique
`<body onresize=print()>` -> execute using exploit server in iframe

Mine:
`<body oncontentvisibilityautostatechange=print() style=display:block;content-visibility:auto>"` -> works without exploit server without user interaction.
## 6. Impact
Attacker can run arbitrary javascript in victim's browser that can lead to account takeover, session hijacking, and phishing.

## 7. Reusable Pattern
Check if security measurements such as WAF filter all tags, attributes, etc. Also check if error reveal too much information that can lead to enumeration.

## 8. Key Takeaway
Do not reveal too much information on errors that can lead to enumeration. Try to filter all dangerous tags and filters using technologies like WAF.

