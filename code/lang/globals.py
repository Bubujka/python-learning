#!/usr/bin/env python3
"""
Глобальные переменные в приложении
"""

greet = 'Здрасти'
def hello(name):
    global greet
    print(greet, name)

def ololo():
    print(globals())


hello('zuzujka')
ololo()
