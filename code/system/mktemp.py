#!/usr/bin/env python3
"""
Создать временный файл
"""
import tempfile

with tempfile.TemporaryFile() as f:
    f.write(b'hello wrld')
    f.seek(0)
    print(f.read())
