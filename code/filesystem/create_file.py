#!/usr/bin/env python3
"""
Создать пустой файл
"""

import glob

open("_tmp/hello.txt", "a").close()

print(glob.glob('_tmp/*'))
