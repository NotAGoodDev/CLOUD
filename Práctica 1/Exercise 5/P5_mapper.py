#!/usr/bin/python3

import sys
import re

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    line = line.replace(", ", '-')
    line = line.replace(',,', ',0,')
    row = re.split(",", line)
    type = row[2]
    mass = row[4]

    print(type + "\t" + mass + "\t1")