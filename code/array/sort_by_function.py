#!/usr/bin/env python3
"""
Отсортировать массив по замыканию
"""

users = [{'name': 'bubujka', 'age': 23},
         {'name': 'zuzujka', 'age': 26},
         {'name': 'jujujka', 'age': 29},
         {'name': 'huhujka', 'age': 18}]

def age(i):
    return i['age']
print(sorted(users, key=age))


