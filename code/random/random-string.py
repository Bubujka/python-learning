#!/usr/bin/env python3
"""Случайная строка"""

import random

print("".join(random.choices('abcdefghij', k=5)))

