#!/usr/bin/env python3
"""
Получить значение из словаря, если его нет - не падать
"""

ME = { "name": "bubujka", 'age': 23 }
print(ME.get('name'))
print(ME.get('sex'))


