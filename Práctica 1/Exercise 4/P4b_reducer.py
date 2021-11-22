#!/usr/bin/python3

import sys

previous = None

for line in sys.stdin:
    key, value = line.split( '\t' )

    if key != previous:
        if previous is not None:
            print("Range: " + str(previous) + "\t" + str(value))
        previous = key
    
    print("Range: " + str(previous) + "\t" + str(value))