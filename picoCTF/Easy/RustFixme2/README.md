# Rust Fixme 2 | picoCTF
## Analysis
We are given rust code with problems, which we need to solve.

## With help of Chatgpt I found out that we need to solve the following issues:
```
1) let party_foul = String::from("Using memory unsafe languages is a: ");
2) decrypt(encrypted_buffer,  &party_foul);
3) fn decrypt(encrypted_buffer:Vec<u8>, borrowed_string: &String){
```
These command should use mutable reference, so they become:
```
1) let mut party_foul = String::from("Using memory unsafe languages is a: ");
2) decrypt(encrypted_buffer,  &mut party_foul);
3) fn decrypt(encrypted_buffer:Vec<u8>, borrowed_string: &mut String){
```

## Solution
After solving those problems we get the flag for this CTF:

picoCTF{4r3_y0u_h4v1n5_fun_y31?}


