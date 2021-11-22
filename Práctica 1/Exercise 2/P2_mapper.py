#!/usr/bin/python3

import sys
import re

#Absolute freq
for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    urls = re.split(" - - ", line)
    splitedUrls = urls[0]
    print(splitedUrls + "\t1")