#!/usr/bin/env python3
"""
Записать что-то в stderr
"""

import sys

print("stdout")
print("stdout2")
print("stderr", file=sys.stderr)
print("stderr2", file=sys.stderr)


