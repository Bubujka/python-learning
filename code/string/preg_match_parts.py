#!/usr/bin/env python3
"""
Разобрать строку по регулярному выражению и получить части
"""

import re

s = "Name: bubujka, age: 23, gender: male"
s2 = "Name: zuzujka, age: -13, gender: notmale"

name, age, gender = re.match("Name: ([a-z]+), age: (-?\d+), gender: (.*)", s).groups()

print(name, age, gender)
