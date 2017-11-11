#!/usr/bin/env python3
"""
Проверить что у объекта есть свойство
"""

class User():
    pass

me = User()
me.username = 'bubujka'

print(hasattr(me, 'username'))
print(hasattr(me, 'age'))


