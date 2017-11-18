#!/usr/bin/env python3
"""Разархивировать строку"""

import gzip

with gzip.open('_stub/gzip.txt.gz') as f:
    print(f.read())


