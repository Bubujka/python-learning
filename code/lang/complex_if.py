#!/usr/bin/env python3
"""
Комплексные условия в if (and, or)
"""

if True and True and False:
    print("NOPE")

if not True or False:
    print("NOPE")

if None or None or 1:
    print("yeeep")


