#!/usr/bin/python3

import sys

previous = None
sum = 0
total = 0.0;

for line in sys.stdin:
    key, value, times = line.split( '\t' )

    if key != previous:
        if previous is not None:
            print(str(previous) + "\t" + str(total/sum))
        previous = key
        sum = 0
        total = 0
        
    
    sum = sum + int( times )
    total = total + float(value)
    

print(str(previous) + "\t" + str(total/sum))
