#!/usr/bin/env python3
"""
Вызов функции с передачей параметров в виде массива
"""

def printer(name, age, sex):
    print("Name: ", name)
    print("Age: ", age)
    print("Sex: ", sex)

arr = ['bubujka', 27, True]
printer(*arr)


