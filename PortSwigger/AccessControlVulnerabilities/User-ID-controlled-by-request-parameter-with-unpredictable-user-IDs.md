# Challenge Name: User ID controlled by request parameter, with unpredictable user IDs 
# Platform: PortSwigger
# Difficulty: Apprentice

## 1. Vulnerability Type
IDOR - Horizontal Privilege Escalation

## 2. Root Cause
Application does not verify that the requested user ID belongs to the authenticated user.

## 3. Attack Surface
`/my-account?id=`

## 4. Exploit Method
Under `/post?postId=3` we can move to `carlos`'s blog on `/blogs?userId=1ad7385c-2933-4b9f-bcef-44daef0201cf` endpoint. This endpoint leaks `GUID` of user `carlos`. After getting `carlos`'s `GUID` it is possible for authenticated user go to `My account` and replace original `GUID` with victim's `GUID`.

## 5. Payload / Technique
`/my-account?id=1ad7385c-2933-4b9f-bcef-44daef0201cf`

## 6. Impact
Unauthorized access to other users sensitive data such as API key, PII (personally identifiable information), etc. In real world application can lead to severe user data leak, financial loss, data theft.

## 7. Reusable Pattern
If application leaks users' `GUID` and  does not verify authorization of users using server-side source ownership, it is possible to modify parameters like id and get access to existing user accounts, data, etc.

## 8. Key Takeaway
Always validate authentication and authorization server-side using at least session cookies and JWT tokens. Do not blindly trust user requests and its parameters without proper validation.
