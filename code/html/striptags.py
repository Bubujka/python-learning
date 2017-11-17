#!/usr/bin/env python3
"""Вырезать html теги"""

from bs4 import BeautifulSoup
html = open('_stub/sample.html').read()

soup = BeautifulSoup(html, 'html.parser')
print(soup.get_text())


