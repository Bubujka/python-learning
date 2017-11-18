#!/usr/bin/env python3
"""
Парсить csv как массив объектов
"""

import csv

with open('_stub/file.csv') as tfile:
    r = csv.DictReader(tfile)
    for line in r:
        print(line)

