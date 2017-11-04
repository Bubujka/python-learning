#!/usr/bin/env python3
"""
Оборвать цикл
"""

arr = [1, 2, 3, 'stop', 4, 5]
for i in arr:
    if i is 'stop':
        break
    print("- ", i)

