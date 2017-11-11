#!/usr/bin/env python3
"""
Скачать файл по ссылке и положить на диск
"""

import shutil
from urllib.request import urlopen

URL = 'http://my.bubujka.org'
with urlopen(URL) as src, open("_tmp/index.html", "wb") as out:
    shutil.copyfileobj(src, out)


