#!/usr/bin/env python3
"""
Вызвать команду и получить то что она вывела
"""
from subprocess import check_output as c

t = c(['ls', '-l'])
print(t.decode('utf-8'))
