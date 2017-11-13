#!/usr/bin/env python3
"""Проверить что путь - это ссылка"""

import os

print(os.path.islink('_stub/directory'))

print(os.path.islink('_stub/symlink'))


