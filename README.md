# py-prettyfbmsg

Make Facebook messages pretty again.

## WTF?

Even copy-pasted messages directly from Facebook/Messenger? I am sure you did. Unless you are using some awesome hacks, this is how they looks like when pasted in text editor.

```
$ cat aasifkhanchowdhury.txt
Md Minhazul Haque
12:14am
Md Minhazul Haque
Hello smile emoticon
A Asif Khan Chowdhury
12:14am
A Asif Khan Chowdhury
Hi grin emoticon
Md Minhazul Haque
12:14am
Md Minhazul Haque
How is it going?
A Asif Khan Chowdhury
12:14am
A Asif Khan Chowdhury
Fine.
Md Minhazul Haque
12:15am
Md Minhazul Haque
Thanks.
```

Ever wondered what if you could remove those timestamps between names and remove duplicate entries? And change the way the name of you and your friend appears? I think there is a way of doing that. I present the script - `prettyfbmsg.py`.

## How does it work?

Pass the name of a plain text file you have saved the conversations in to the script. Here is an example.

```
$ python prettyfbmsg.py aasifkhanchowdhury.txt
● Hello
○ Hi
● How is it going?
○ Fine.
● Thanks.
```

Fun, right?

## License

[WTFPL](http://www.wtfpl.net/txt/copying/)
