#!/usr/bin/env python3
"""
Произвольное число аргументов в функцию
"""

def hello(greet, *args):
    print(greet, ", ".join(args))

hello('Здравствуйте', 'bubujka', 'jujujka', 'zuzujka')


