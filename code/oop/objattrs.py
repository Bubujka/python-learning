#!/usr/bin/env python3
"""Получить все аттрибуты объекта"""

class User():
    """Тестируем класс"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        """Поздороваться"""
        print("Hello from ", self.name)


u = User('Bubujka', 12);

print( dir(u) )



