#!/usr/bin/env python3
"""
Вызвать внешнюю программу
"""

from subprocess import check_output

t = check_output(['ls', '-l'])
print(t.decode('utf-8'))


