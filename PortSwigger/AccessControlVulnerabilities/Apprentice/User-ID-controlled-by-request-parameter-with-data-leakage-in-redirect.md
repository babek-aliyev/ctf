# Challenge Name: User ID controlled by request parameter with data leakage in redirect 
# Platform: PortSwigger
# Difficulty: Apprentice

## 1. Vulnerability Type
IDOR

## 2. Root Cause
Application reveals sensitive user data in redirect response without using authorization and server-side ownership validation.

## 3. Attack Surface
`/my-account?id=`

## 4. Exploit Method
First step should be normal login process. After logging in web application uses `/my-account?id=` redirect to another page. However, if client changes the `id` to another existing `id`, application will reveal `username` and `API key` of another user.

## 5. Payload / Technique
`/my-account?id=carlos`

## 6. Impact
Unauthorized user can view sensitive data belonging to other users without proper server-side ownership validation which can lead to data leak, financial loss, etc.

## 7. Reusable Pattern
Checking redirect responses in application that does not use proper server-side ownership validation and authorization can leak data that is sensitive or might be useful to gain sensitive data.

## 8. Key Takeaway
Always validate authorization and ownership server-side without revealing any personal identifiable information and sensitive data like `API key`.


