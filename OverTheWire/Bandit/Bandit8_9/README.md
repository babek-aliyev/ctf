# Bandit Level 8=> Level 9 | OverTheWire
## Description
The password for the next level is stored in the file data.txt and is the only line of text that occurs only once.

## Analysis
The `data.txt` file has lots of lines of duplicated strings which has only one unique password among them. To solve the current CTF challenge we need to introduce **piping**. Piping is a powerful command-line feature that enables forwarding output of one command to the input of another command. To **pipe** two commands we need to use `|` (vertical bar) symbol. Now, how will we use piping here? Let's see the solution below:
```bash
bandit8@bandit:~$ sort data.txt | uniq -u
4CKMh1--------------------------
bandit8@bandit:~$ 
```
Now let's analyze the command:
* `sort data.txt` => this command takes `data.txt` file and sorts it alphabetically. After running this command we have all duplicate strings sorted out with our password among them.
* `|` => piping takes the input from `sort data.txt` and forwards it to the output of `uniq -u`
* `uniq -u` => this command filters adjacent matching lines from input. This means that if we don't do sorting first, `uniq` command will not work. `-u` flag filters the input and prints only unique lines.

As the password in `data.txt` file was unique and occured only once, the combination of these commands gave us the password for bandit9!
