# Challenge Name: Password reset poisoning via middleware
# Platform: PortSwigger
# Difficulty: Practitioner

## 1. Vulnerability Type
Password Reset Poisoning

## 2. Root Cause
The application trusts the `X-Forwarded-Host` header when generating password reset links.

Because this value is not validated, an attacker can modify the host used in the reset URL and redirect the token to an attacker-controlled server.
## 3. Attack Surface
`/forgot-password`

## 4. Exploit Method
The attacker submits a password reset request for the victim account.

By adding the `X-Forwarded-Host` header, the attacker changes the host used when the application generates the reset link.

The application sends an email to the victim containing a reset link that points to the attacker's server.

When the victim clicks the link, the reset token is sent to the attacker's exploit server.

The attacker can then use the token to reset the victim's password and gain access to the account.
## 5. Payload / Technique
Password reset poisoning using X-Forwarded-Host header to control the reset link host.
## 6. Impact
Password reset poisoning allows attackers to steal reset tokens and perform account takeover.
## 7. Reusable Pattern
When testing password reset functionality, verify whether headers such as X-Forwarded-Host or Host are used to generate reset links without validation.
## 8. Key Takeaway
Applications must not trust user-controlled headers when generating sensitive URLs such as password reset links.

