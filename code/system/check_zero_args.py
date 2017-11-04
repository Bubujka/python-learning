#!/usr/bin/env python3
"""
Проверить что передано 0 аргументов
"""

import sys

if len(sys.argv) == 1:
    print("Не передано аргументов")
else:
    print("Передано аргументов:", len(sys.argv) - 1)

