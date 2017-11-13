#!/usr/bin/env python3
"""Индексировать массив"""

users = [
    { 'name': 'bubujka', 'age': 27 },
    { 'name': 'zuzujka', 'age': 28 },
    { 'name': 'jujujka', 'age': 25 },
    { 'name': 'cucujka', 'age': 23 },
]

print({ v['name']: v for v in users })


