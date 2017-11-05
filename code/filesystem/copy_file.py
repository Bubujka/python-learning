#!/usr/bin/env python3
"""
Скопировать файл
"""

from glob import glob
import shutil
import os

shutil.rmtree('_tmp', True)
os.makedirs('_tmp')
open('_tmp/.gitkeep', 'w').close()

print(glob('_tmp/*'))

open('_tmp/one.txt', 'w').close()

print(glob('_tmp/**', recursive=True))

shutil.copy('_tmp/one.txt', '_tmp/two.txt')

print(glob('_tmp/**', recursive=True))
