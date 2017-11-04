#!/usr/bin/env python3
"""
Экранирование аргументов для shell команды
"""
import shlex
print(shlex.quote("""rm -rf ' " ( ) " \ """))

