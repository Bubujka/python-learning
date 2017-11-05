#!/usr/bin/env python3
"""
Скопировать рекурсивно папку в другое место
"""

import helpers
import os
import shutil

helpers.clear_tmp()

os.makedirs('_tmp/one/two/three')
open('_tmp/one/two/three/hello.txt', 'w').close()

shutil.copytree('_tmp/one', '_tmp/abc')

helpers.tmp_contents()
