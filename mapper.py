#!/usr/bin/env python3
import sys
next(sys.stdin) # skip the first row
for line in sys.stdin:
    line = line.strip().split(',')
    product=line[1]
    print(f"{product}\t1")
    

