#!/usr/bin/env python3
"""
Как вызывать метод у объекта
"""

class User():
    def __init__(self):
        pass

    def hi(self):
        print("Helo {}!".format(self))

me = User()
me.hi()


