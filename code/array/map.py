#!/usr/bin/env python3
"""
Преобразовать один массив в другой
"""

def bang(what):
    return what+"!"

arr = ["bubujka", "zuzujka"];

print([bang(x) for x in arr])
print(list(map(bang, arr)))
