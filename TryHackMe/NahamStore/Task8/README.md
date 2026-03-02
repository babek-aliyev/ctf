# Challenge Name: NahamStore | Task 8
# Platform: TryHackMe
# Difficulty: Medium

## 1. Vulnerability Type
LFI (Local File Inclusion)
## 2. Root Cause
The application directly uses user-supplied input in file path operations without proper validation or path restriction.
## 3. Attack Surface
`/product/picture/?file=`

## 4. Exploit Method
Fuzzed endpoint using `/usr/share/seclists/Fuzzing/LFI/LFI-Jhaddix.txt` wordlist.

## 5. Payload / Technique
```bash
┌──(kali㉿kali)-[/usr/share/seclists/Fuzzing/LFI]
└─$ ffuf -u "http://nahamstore.thm/product/picture/?file=FUZZ" \
-w /usr/share/seclists/Fuzzing/LFI/LFI-Jhaddix.txt -fs 19
```
## 6. Impact
Possible impact:
* Read `/etc/passwd`
* Read configuration files
* Read application source code
* Read API key
* Remote Code Execution (RCE)
* Leak database credentials
## 7. Reusable Pattern
Identify endpoints that load files dynamically (e.g., image loaders, download endpoints, export features) and test for directory traversal using automated fuzzing and traversal payloads.
## 8. Key Takeaway
* Enforce strict directory whitelisting
* Normalize paths before use
* Reject `../` sequences
* Use safe file mapping (e.g. IDs instead of file paths)
* Disable dangerous wrappers (if PHP)
