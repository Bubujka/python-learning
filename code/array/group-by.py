#!/usr/bin/env python3
"""Сгруппировать массив"""

import itertools

data = [
        { 'id': 1, 'company': 'alfa' },
        { 'id': 2, 'company': 'beta' },
        { 'id': 3, 'company': 'hamma' },
        { 'id': 4, 'company': 'alfa' },
        { 'id': 5, 'company': 'beta' },
        { 'id': 6, 'company': 'hamma' }
        ]

def keyfn(t):
    return t['company']
data = sorted(data, key=keyfn)
for k, v in itertools.groupby(data, key=keyfn):
    print(k, list(v))


