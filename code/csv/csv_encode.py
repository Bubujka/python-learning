#!/usr/bin/env python3
"""
Сериализация в csv
"""

headers = ['id', 'username', 'age']
data = [
  [1, 'bubujka', 23],
  [2, 'jujujka', 25],
  [3, 'zuzujka', 28],
  [4, 'wuwujka', 29]]

import csv

with open('_tmp/test.csv', 'w') as tfile:
    w = csv.writer(tfile)
    w.writerow(headers)
    for line in data:
        w.writerow(line)

with open('_tmp/test.csv') as tfile:
    print(tfile.read())





