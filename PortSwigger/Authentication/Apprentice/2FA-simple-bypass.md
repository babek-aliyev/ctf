# Challenge Name: 2FA simple bypass 
# Platform: PortSwigger
# Difficulty: Apprentice

## 1. Vulnerability Type
2FA Bypass - Account Takeover

## 2. Root Cause
Application does not properly enforce the second authentication step server-side, allowing access to authenticated endpoints without completing 2FA.
## 3. Attack Surface
`/login2`
`/my-account`
## 4. Exploit Method
After submitting valid username and password, the application redirects
to /login2 to complete the second authentication step.

However, the server does not verify whether the 2FA step was completed.
If the attacker directly requests /my-account, the server grants access
without checking the 2FA code.
## 5. Payload / Technique
Request modification.

## 6. Impact
Attackers who know valid credentials can bypass 2FA and gain full access to the victim's account. This can lead to account takeover, data leak, data loss, financial loss, etc.

## 7. Reusable Pattern
If an application uses multi-step authentication, try accessing protected endpoints directly without completing all authentication steps.
## 8. Key Takeaway
Always enforce authentication steps server-side and verify that the user has completed 2FA before granting access to protected endpoints.

