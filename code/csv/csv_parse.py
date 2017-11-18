#!/usr/bin/env python3
"""
Разбор csv
"""

import csv

with open('_stub/file.csv') as f:
    r = csv.reader(f)
    for line in r:
        print(", ".join(line))

