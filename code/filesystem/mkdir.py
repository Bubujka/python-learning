#!/usr/bin/env python3
"""
Создать каталог
"""

import os
import pprint
import shutil
from glob import glob

pp = pprint.PrettyPrinter().pprint

shutil.rmtree('_tmp/my', ignore_errors=True)

pp(glob('_tmp/**', recursive=True))

os.makedirs('_tmp/my/super/deep/dir', exist_ok=True)

pp(glob('_tmp/**', recursive=True))

