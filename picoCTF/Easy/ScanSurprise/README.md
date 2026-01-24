# Scan Surprise | picoCTF

## Analysis

After connecting to machine via ssh in this CTF we can observe that it has an image:
```bash
ctf-player@challenge:~/drop-in$ ls
ctf-player@challenge:~/drop-in$ flag.png
```
## Solution

While connecting to this machine, we got a QR Code image, which means the `flag.png` might also be a QR code. After some research, I found that we can use tool name `zbarimg` to decode QR Code image.

## Answer

We need to run the following command:
```bash
ctf-player@challenge:~/drop-in$ zbarimg flag.png 
Connection Error (Failed to connect to socket /var/run/dbus/system_bus_socket: No such file or directory)
Connection Null
QR-Code:picoCTF{--------------------}
scanned 1 barcode symbols from 1 images in 0.01 seconds
```
As you can see we decoded the flag for this CTF!!

