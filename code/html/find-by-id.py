#!/usr/bin/env python3
"""Найти в html элемент по id"""

from bs4 import BeautifulSoup
html = open("_stub/sample.html").read()
soup = BeautifulSoup(html, 'html.parser')

print(soup.find_all(id='li3'))
