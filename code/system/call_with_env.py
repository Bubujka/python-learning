#!/usr/bin/env python3
"""
Вызвать консольную команду и переопределить для неё переменные окружения
"""

from subprocess import call
import os
os.putenv("HELO", "FUCKING WRLD")
call("export", shell = True)


