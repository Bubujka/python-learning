#!/usr/bin/env python3
"""
Получить md5 от строки
"""
import hashlib
print(hashlib.md5('bubujka'.encode('utf-8')).hexdigest())

