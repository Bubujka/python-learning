#!/usr/bin/env python3
"""
Изменить права на файл
"""
import os

open('_tmp/file.txt', 'w').close()
print(oct(os.stat('_tmp/file.txt').st_mode))

os.chmod('_tmp/file.txt', 0o777)

print(oct(os.stat('_tmp/file.txt').st_mode))
os.chmod('_tmp/file.txt', 0o644)

