#!/usr/bin/python3

import sys
import re
import math

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    ratings = re.split("\t", line)
    
    print(str(math.ceil(float(ratings[1]))) + "\t" + str(ratings[0]))