#!/usr/bin/env python3
"""
Проверить что файл пустой
"""
import os.path
def check(f):
    print("File ", f, "empty?:", bool(os.path.getsize(f)))

check('_stub/dirs.txt')
check('_stub/empty.txt')
