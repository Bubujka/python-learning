#!/usr/bin/env python3
"""
Удалить переменную
"""

name = "bubujka"
print("name" in locals())
del name
print("name" in locals())

