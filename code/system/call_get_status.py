#!/usr/bin/env python3
"""
Получить статус выполнения команды
"""
import subprocess

try:
    t = subprocess.check_output(['ls', 'ololo'])
except subprocess.CalledProcessError as err:
    print("Status code {}".format(err.returncode))

