#!/usr/bin/env python3
"""Прогрессбар консольный"""

import time
import progressbar

bar = progressbar.ProgressBar()
arr =  [1,2,3,4,5,6,7,8,9,10,11,12]
for i in bar(arr):
    time.sleep(0.2)
