# Challenge Name: NahamStore | Task 7
# Platform: TryHackMe
# Difficulty: Medium

## 1. Vulnerability Type
IDOR
## 2. Root Cause
Missing server-side authorization check: the application fails to validate ownership of resources (address, order) before returning data and trusts client-supplied identifiers.

## 3. Attack Surface
Address: `/basket` -> `address_id`
Order: `/account/orders/{id}`. PDF receipt endpoint using `what` and `id`
## 4. Exploit Method
Address: Intercept the request and modify the `address_id` parameter to reference another user's address.
Order: Manipulate the `id` parameter and inject an additional `user_id` parameter via **URL encoding** to access another user's receipt.
## 5. Payload / Technique
Address: `address_id`
Order: `what=order&id=3%26user_id%3d3`
## 6. Impact
Unauthorized access to other users’ addresses and order receipts, leading to disclosure of personally identifiable information (PII).

## 7. Reusable Pattern
Test all object references (path parameters, query parameters, hidden fields, PDF generators, export functions) by modifying IDs and injecting additional parameters to bypass ownership checks.

## 8. Key Takeaway
Enforce server-side authorization by validating resource ownership (e.g., ensure `order.user_id == authenticated_user_id`) before returning data.
