#!/usr/bin/python3

import sys
import re

#@ Year and Close stock
firstLine = True    #Dont know how to do like a matrix -> [1:]

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    row = re.split("-", line)
    year = row[0]
    close = re.split(",", line)
    
    if(firstLine):
        firstLine = False
    else:
        print(year + "\t" + close[4] + "\t1")
