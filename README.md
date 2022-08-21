# ytid
A Python script that outputs the YouTube ID of a YouTube channel.

## Command
```bash
$ python3 yt-id.py URL
```
## URL formats
URL can come in a few different formats, all of which are handled by the script:
- https://www.youtube.com/watch?v=dQw4w9WgXcQ (video link)
- https://www.youtube.com/user/PewDiePie (user link)
- https://www.youtube.com/c/LeParisien (channel link)
- https://www.youtube.com/hunantv (channel custom link)

## Improvements
I created an alias command in my .bashrc file, so that the script is easily callable.
I added the following line:
```text
alias ytid="python3 /path/to/the/script/yt-id.py"
```
To apply changes, either reboot your machine, or type the following command:
```bash
$ source ~/.bashrc
```
This new line in your .bashrc file enables the following command to be typed:
```bash
ytid URL
```
Efficient, innit?
