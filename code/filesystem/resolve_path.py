#!/usr/bin/env python3
"""
Раскрыть относительный путь в абсолютный
"""
from os import path
print(path.abspath('../bin/'))
print(path.abspath('/home/bubujka/../zuzujka/.'))

