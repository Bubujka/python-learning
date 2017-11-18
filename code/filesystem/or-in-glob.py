#!/usr/bin/env python3
"""Или в glob выражении"""

from glob import glob

print(glob('_stub/*.txt') + glob('_stub/*.doc'))

