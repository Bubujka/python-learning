#!/usr/bin/env python3
"""
Бесконечный цикл
"""
import time

i = 0
while True:
    print("Tick ({})...".format(i), flush=True)
    time.sleep(0.2)
    i += 1
    if i is 10:
        break


