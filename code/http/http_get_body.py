#!/usr/bin/env python3
"""
Сделать запрос и получить строку из ответа
"""

from urllib.request import urlopen
print(urlopen('http://my.bubujka.org').read().decode('utf-8'))

