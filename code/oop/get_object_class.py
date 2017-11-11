#!/usr/bin/env python3
"""
Получить класс объекта
"""

class User():
    pass

class Dog():
    pass

me = User()
pluto = Dog()

print(type(me))
print(type(pluto))
print(type(13))

print(me.__class__)
print(me.__class__.__name__)




