#!/usr/bin/env python3
"""
Итерация по строкам в stdin
"""

import fileinput
import sys

for line in sys.stdin:
    print("Received: {}".format(line.strip()))

