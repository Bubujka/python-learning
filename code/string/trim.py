#!/usr/bin/env python3
"""
Обрезать пробелы с начала-конца строки
"""

name = " \t \n bubujka \t \n \t "

print('|'+name+'|')
print('|'+name.lstrip()+'|')
print('|'+name.rstrip()+'|')
print('|'+name.strip()+'|')


