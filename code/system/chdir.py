#!/usr/bin/env python3
"""
Переход в другой каталог
"""

import os
from glob import glob

print(glob('*'))

os.chdir('..')

print(glob('*'))


