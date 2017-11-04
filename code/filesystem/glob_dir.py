#!/usr/bin/env python3
"""
Получить список файлов в каталоге по glob выражению
"""

import glob

print(glob.glob('_stub/*.txt'))
print(glob.glob('_stub/**/*.txt', recursive=True))
print(glob.glob('_stub/*'))


