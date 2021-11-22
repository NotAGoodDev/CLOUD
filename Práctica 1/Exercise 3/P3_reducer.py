#!/usr/bin/python3

import sys

previous = None
sum = 0
days = 0

for line in sys.stdin:
    key, value, times = line.split( '\t' )
    
    if key != previous:
        if previous is not None:
            print(str(sum / days) + '\t' + previous)
        previous = key
        sum = 0
        days = 0
    
    sum = sum + float( value )
    days = days + int (times)

print (str(sum / days) + '\t' + previous)