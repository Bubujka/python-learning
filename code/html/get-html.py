#!/usr/bin/env python3
"""Получить innerHTML"""

from bs4 import BeautifulSoup
html = open("_stub/sample.html").read()
soup = BeautifulSoup(html, 'html.parser')


print(soup.ul.decode_contents())
print("".join(str(t) for t in soup.ul.children))
