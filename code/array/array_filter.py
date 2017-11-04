#!/usr/bin/env python3
"""
Отфильтровать массив по замыканию-функции
"""
arr = list(range(1,13))
print([x for x in arr if x % 3 is 0])


