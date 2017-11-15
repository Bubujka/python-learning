#!/usr/bin/env python3
"""Получить аттрибут"""

from bs4 import BeautifulSoup
html = open("_stub/sample.html").read()
soup = BeautifulSoup(html, 'html.parser')

print(soup.a['href'])


