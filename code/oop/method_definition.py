#!/usr/bin/env python3
"""
Добавить в класс - функцию
"""

class User():
    def __init__(self, name):
        self.name = name

    def hi(self):
        print("Hello from", self.name)

me = User('Bubujka')
me.hi()

