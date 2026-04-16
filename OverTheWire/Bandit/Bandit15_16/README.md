# Bandit Level 15=> Level 16 | OverTheWire
## Description
The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL/TLS encryption.
## Analysis
Similar to previous level, we do not get anything useful on this machine. According to the description of this lab, we should connect to localhost port 30001 using SSL/TLS. To do so, we can use command `openssl`.

## Solution
We should use the following command template to connect to localhost using SSL/TLS:
```bash
openssl s_client -connect host:port
```
Here, `openssl s_client` creates encrypted channel to the provided host. Without this encryption inputs are going in plain text. In this lab our command will look like this:
```bash 
openssl s_client -connect 127.0.0.1:30001
```

After this command it will require password of `bandit15`. Submitting it will reveal the password of the next machine!
