# [Server-side template injection using documentation] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-18
 
---
 
## Vulnerability / core concept
Server-side Template Injection

## What made me stuck
This level was not a quick one, but with research I was consistent and solved this lab.
 
## What unblocked me
`null`
 
---


## Attack path
1) First we need to log in to our content-manager account so we can access template edit functionality.
2) While inspecting this I noticed `${expression}` in the template. At first, I thought this is JS template. Then I decided to test `${alert(1)}` and this revealed errors with `freemaker.core` and `freemaker.template`. This instantly revealed that my first assumption was wrong and the underlying framework is `Freemaker`.
3) After successful information gathering, I started to google for Freemaker documentation and its dangerous commands that people used to exploit real systems. I found a blog where pentester showed the payload that he used: `${"freemarker.template.utility.Execute"?new()("rm /home/carlos/morale.txt")}`. In his case, he used `?lower_abc` function to encoded character-by-character and bypass restricted characters. In our case, we did not need encoding as payload worked without checking dangerous characters.
4) Now all we need to do is to use that payload and delete carlos's `morale.txt` file from his home directory.

---


## Payload / key command
Instead of `${product.name}` we write `${"freemarker.template.utility.Execute"?new()("rm /home/carlos/morale.txt")}`. This payload instantiates FreeMarker's built-in `Execute` utility class and calls it with `rm /home/carlos/morale.txt` as the argument, which runs that as an OS command — deleting the file `morale.txt` from `/home/carlos` on the server.

---


## What I'd recognize faster next time
Trying to break the application and squeeze any error from it that we can. Like in this lab, if I did not get those error messages, my assumption about the template engine would be wrong and I would not be able to exploit it.


