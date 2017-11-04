#!/usr/bin/env python3
"""
Записать строку в файл
"""

text = """Hello
fucking
world
"""

with open("_tmp/writing.txt", "w") as f:
    f.write(text)

with open("_tmp/writing.txt") as f:
    print(f.read())
