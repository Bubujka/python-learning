#!/usr/bin/env python3
"""
Удалить файл
"""

import os
from glob import glob

print(glob('_tmp/*'))
open("_tmp/hello.txt", "w").close()
print(glob('_tmp/*'))

os.unlink("_tmp/hello.txt")

print(glob('_tmp/*'))
