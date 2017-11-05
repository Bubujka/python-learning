#!/usr/bin/env python3
"""
Создать symbolic link
"""

import os
from subprocess import call

call('rm -rf _tmp/*', shell = True)

os.symlink('_tmp/ololo/hi/hi', '_tmp/hello.txt')

call(['ls', '-l', '_tmp'])

