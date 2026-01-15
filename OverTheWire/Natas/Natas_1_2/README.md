🕵️ Natas Level 2 → Level 3 Walkthrough

The page initially displays the message “There is nothing on this page.”
![intro](images/natas2.jpg)
However, we should never trust what the frontend shows.

Inspect the page source

Open the browser developer tools (Ctrl + Shift + I)
![folder](images/folder.png)


In the HTML <body> section, there is an image tag:

<img src="files/pixel.png">


Identify hidden directory

The image path reveals a folder named files

Navigate to /files in the browser
![directory](images/directory.jpg)


Explore the directory contents

Inside the directory, a file named user.txt is available

Retrieve the password

Open user.txt
![answer](images/answer.jpg)

The password for natas3 is stored inside