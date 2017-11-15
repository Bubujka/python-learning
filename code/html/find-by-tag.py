#!/usr/bin/env python3
"""Найти элемент по тэгу"""

from bs4 import BeautifulSoup
html = open("_stub/sample.html").read()
soup = BeautifulSoup(html, 'html.parser')

print(soup.li)
print(soup.find_all('li'))


