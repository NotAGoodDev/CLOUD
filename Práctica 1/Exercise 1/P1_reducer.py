#!/usr/bin/python3

import sys

previous = None

for line in sys.stdin:
    key, value = line.split( '\t' )
    
    if key != previous:
        if previous is not None:
            print(str(previous))
        previous = key
    
    
print(str(previous))