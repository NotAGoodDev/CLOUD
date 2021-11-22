#!/usr/bin/python3

import sys

previous = None
sum = 0
totalMass = 0

for line in sys.stdin:
    key, value, times = line.split( '\t' )
    
    if key != previous:
        if previous is not None:
            print (str(float(totalMass/sum)) + '\t' + previous)
        previous = key
        sum = 0
        totalMass = 0
    
    sum = sum + int( times )
    totalMass = totalMass + float(value)

print (str(float(totalMass/sum)) + '\t' + previous)