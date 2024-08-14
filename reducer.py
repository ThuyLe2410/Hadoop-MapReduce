#!/usr/bin/env python3
import sys

cur_product = None
product = None
cur_count = 0
for row in sys.stdin:
    row=row.strip()
    product, count = row.split("\t",1)
    product = product.strip()
    try:
        count = int(count)
    except ValueError:
        continue
    if cur_product==product:
        cur_count += count
    else:
        if cur_product:
            print(f"{cur_product}\t{cur_count}")
        cur_product = product
        cur_count = count
if cur_product == product:
    print(f"{cur_product}\t{cur_count}")

        
    

