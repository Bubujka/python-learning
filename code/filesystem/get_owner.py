#!/usr/bin/env python3
"""
Получить владельца файла
"""

import os
import pwd
print( pwd.getpwuid(os.stat(__file__).st_uid).pw_name )



