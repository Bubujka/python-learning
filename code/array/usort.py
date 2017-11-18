#!/usr/bin/env python3
"""Отсортировать по функции сравнения"""

import functools

ints = [*range(1,15)]
def mycmp(a, b):
    if a == 13:
        return -1
    if a < b:
        return -1
    elif a > b:
        return 1
    return 0

print(sorted(ints))

print( sorted(ints, key=functools.cmp_to_key(mycmp)) )
