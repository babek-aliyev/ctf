# Challenge Name: Insecure direct object references 
# Platform: PortSwigger
# Difficulty: Apprentice

## 1. Vulnerability Type
IDOR (Insecure Direct Object Reference)

## 2. Root Cause
Web application does not check for authorization or ownership when retrieving transcript of conversation. 

## 3. Attack Surface
`/download-transcript/`

## 4. Exploit Method
After pressing `View transcript` and intercepting traffic, attacker can observe `/download-transcript/` endpoint that returns `.txt` files. It does not check for authorization and ownership, which means attacker can download any arbitrary transcripts like `1.txt`, `2.txt`, etc. `number.txt` is transcript file naming convention in this web page. In this lab, `1.txt` was transcript of user `carlos` that contained conversation with admin about password reset and revealed password of `carlos`.
## 5. Payload / Technique
`/download-transcript/1.txt`

## 6. Impact
Unauthenticated, unauthorized user can access victims' chats without server-side ownership validation. This can lead to serious data leak, privacy disclosure, etc.

## 7. Reusable Pattern
If web application does not check authorization and ownership server-side, that means it is possible to manipulate endpoints to gain unauthorized access to other users' data, chats, etc.

## 8. Key Takeaway
Always validate endpoints server-side and make sure to use authorization to check the ownership of file without giving access to anyone.


