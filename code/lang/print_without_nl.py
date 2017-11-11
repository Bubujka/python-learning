#!/usr/bin/env python3
"""
Печать в консоль без перевода строки
"""

def nprint(*args):
    """Печать в консоль без перевода строки"""
    print(*args, end="")

nprint('hello', 'world')
nprint('how')
nprint('are')
nprint('you')

