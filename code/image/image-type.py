#!/usr/bin/env python3
"""Получить тип изображения"""

from PIL import Image
im = Image.open('_stub/me.png')
print(im.format)



