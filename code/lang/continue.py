#!/usr/bin/env python3
"""
Пропустить итерацию в цикле
"""

arr = [1, 2, 3, 'stop', 4, 5]
for i in arr:
    if i is 'stop':
        continue
    print("- ", i)

