#!/usr/bin/env python3
"""
Рекурсивный поиск каталогов
"""
from glob import glob
from os import path

print([x for x in glob('_stub/**', recursive=True) if path.isdir(x)])
