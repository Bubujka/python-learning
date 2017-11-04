#!/usr/bin/env python3
"""
Дописать что-то в файл
"""

text = """Hello
fucking
world
"""

with open("_tmp/writing.txt", "w") as f:
    f.write(text)

with open("_tmp/writing.txt", "a") as f:
    f.write('!!!')

with open("_tmp/writing.txt") as f:
    print(f.read())
