#!/usr/bin/python3

import sys
import re

firstLine = True    #Dont know how to do like a matrix -> [1:]

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    ratings = re.split(",", line)

    userId = ratings[1]
    rate = ratings[2]
    
    if(firstLine):
        firstLine = False
    else:
        print(str(userId) + "\t" + str(rate) + "\t1")