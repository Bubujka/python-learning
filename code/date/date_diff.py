#!/usr/bin/env python3
"""
Сравнение двух дат
"""

import time
now = time.time()
before = time.localtime(now-3600)
after = time.localtime(now+3600)

print(time.localtime(now) < after)
print(before < after)
print(before == after)


