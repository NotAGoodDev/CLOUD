#!/usr/bin/python3

import sys
import re

keyWord = sys.argv[1]

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    words = re.split(r"\W+", line)
    
    for word in words:
        if(word == str(keyWord)):
            print( line.lower() + "\t1" )
            
            ##FALLAAAAA