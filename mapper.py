#!/usr/bin/env python3
import sys

# skip header
header = True

for line in sys.stdin:
    line = line.strip()

    if header:
        header = False
        continue

    fields = line.split(",")

    # dataset columns
    # Store,Date,Weekly_Sales,...

    store = fields[0]
    weekly_sales = fields[2]

    try:
        sales = float(weekly_sales)
        print(f"{store}\t{sales}")
    except:
        continue
