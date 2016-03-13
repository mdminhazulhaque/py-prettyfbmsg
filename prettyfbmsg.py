#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Md. Minhazul Haque
# License: WTFPL

import re
import sys
    
def prettyfbmsg(contents, peer0, peer1):
    regexp0 = peer0 + "\n.*\n" + peer0
    regexp1 = peer1 + "\n.*\n" + peer1

    # remove timestamp
    contents = re.sub(regexp0, peer0, contents)
    contents = re.sub(regexp1, peer1, contents)

    # remove emoticon strings
    contents = re.sub(r"\w+ emoticon", "", contents)
    
    # trim empty newlines
    contents = "\n".join([s for s in contents.split("\n") if s])

    # bullets
    re0 = '●'
    re1 = '○'

    bullet = re0

    for line in contents.split("\n"):
        line = line.strip()
        
        if line:
            # alter bullet when name changes
            if line == peer0:
                bullet = re0
                continue
            elif line == peer1:
                bullet = re1
                continue
            
            print bullet, line

if __name__ == "__main__":
    try:
        with open(sys.argv[1]) as file:
            contents = file.read()
    except:
        print "No input file specified"
        exit(1)
        
    prettyfbmsg(contents, 'Md Minhazul Haque', 'A Asif Khan Chowdhury')
