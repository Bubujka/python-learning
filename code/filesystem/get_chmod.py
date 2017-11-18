#!/usr/bin/env python3
"""
Получить права на файл
"""

import os

stat = os.stat('_stub/executable.sh')
print(oct(stat.st_mode))
