#!/usr/bin/env python3
"""
Зачистить в 0 файл
"""
import os.path

def print_size():
    print(os.path.getsize('_tmp/file.txt'))

with open('_tmp/file.txt', 'w') as f:
    f.write("Helo, wrld")

print_size()

open('_tmp/file.txt', 'w').close()

print_size()

