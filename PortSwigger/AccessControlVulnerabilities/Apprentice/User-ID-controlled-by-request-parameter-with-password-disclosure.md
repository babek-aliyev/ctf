# Challenge Name: User ID controlled by request parameter with password disclosure 
# Platform: PortSwigger
# Difficulty: Apprentice

## 1. Vulnerability Type
IDOR (Insecure Direct Object Reference)

## 2. Root Cause
This web application do not check authorization or ownership, therefore, it is possible for authenticated users access other users' account by modifying `id` in requests. After accessing other users' account, it is possible to view their passwords because of the poorly implemented `Update password` function that shows users' password in plaintext.

## 3. Attack Surface
`/my-account?id=`

## 4. Exploit Method
If unauthorized user changes the `id` value to some existing user's `id`, then user will access victim's account without any server-side authorization and ownership check. Afterwards, by inspecting `Update password` request attacker can retrieve password of victim's account.

## 5. Payload / Technique
`/my-account?id=administrator`

## 6. Impact
Unauthorized attacker will gain access over victim's account. Attacker can also gain access over administrator account the same way, which leads to data leak, potential full administrative access, financial loss, etc.

## 7. Reusable Pattern
If application does not check ownership and authorization server-side, it is possible to modify requiests containing paramteres like `id` to gain unauthorized access over victims' accounts.

## 8. Key Takeaway
Always validate ownership and authorization server-side without trusting the request values from clients because clients can always modify those parameters using proxy tools like Burp Suite, OWASP Zap, etc.


