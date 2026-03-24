# Challenge Name: Broken brute-force protection, multiple credentials per request
# Platform: PortSwigger
# Difficulty: Expert

## 1. Vulnerability Type
Broken Brute-Force Protection / Rate Limit Bypass

## 2. Root Cause
The application applies brute-force protection based on the number of HTTP requests instead of the number of login attempts.

Because the login endpoint accepts JSON input, it is possible to send multiple passwords in a single request using an array. The server checks all values but only counts the request once, allowing the attacker to bypass brute-force protection.

## 3. Attack Surface
`/login`

## 4. Exploit Method
The login request is sent in JSON format.

Instead of sending one password per request, the attacker sends a JSON array containing multiple passwords in the password field.

The server processes each password in the array but only counts the request once for rate limiting.

By sending many passwords in a single request, the attacker bypasses brute-force protection and eventually logs in as the victim.

## 5. Payload / Technique
Password list converted into JSON array format and sent as the password parameter.

Example:
```js
{
  "username": "carlos",
  "password": ["pass1","pass2","pass3","pass4"]
}
```
## 6. Impact
An attacker can bypass brute-force protection and gain unauthorized access to user accounts.

## 7. Reusable Pattern
When testing login endpoints with rate limiting:
- check if JSON input is accepted
- try sending arrays instead of single values
- check if rate limiting counts requests instead of attempts

This may allow brute-force bypass.

## 8. Key Takeaway
Brute-force protection must be applied per authentication attempt, not per HTTP request.
Servers must validate input types and reject unexpected structures such as arrays.
