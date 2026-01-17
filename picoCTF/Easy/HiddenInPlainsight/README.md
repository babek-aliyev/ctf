# Image Metadata & Steganography – CTF Write-up

## Challenge Overview
In this challenge we are given a suspicious `.jpg` image. At first glance, the image reveals no visible clues. The objective is to uncover whether hidden information is embedded within the file and extract the flag.

## Initial Analysis
Opening the image normally yields nothing useful, so the next step is to inspect the file metadata.

To do this, I used `exiftool`, a utility designed to read and display metadata from images and other media files:

```bash
exiftool image.jpg
```
### Discovering Hidden Data
Within the metadata output, a strange comment field appears. It resembles encoded text, so I copied it and tested common decoding methods using CyberChef.

ROT13 → No meaningful output

Base64 → Successful decode

The decoded string revealed:
```
steghide : cEF6endvcmQ=
```
A quick lookup confirmed that steghide is a steganography tool used to hide data inside image and audio files.

The remaining encoded fragment cEF6endvcmQ= clearly appeared to be Base64 as well. Decoding it produced a password:
```
pAzzword
```
### Extracting Embedded Files
Now that we knew the tool and password, the next step was extraction.

Check if the file contains embedded data:
```
steghide info ~/Downloads/img.jpg
```
As expected, the image required a password and confirmed the presence of flag.txt.

Extract the hidden file:
```
steghide extract -sf image.jpg -p pAzzword
```
This successfully extracted flag.txt.

### Retrieving the Flag
To view the contents of the file:

cat flag.txt
The output contained the flag, completing the challenge.

### Conclusion
This CTF demonstrates how metadata analysis and steganography tools like exiftool and steghide can be used to uncover hidden information within files.
