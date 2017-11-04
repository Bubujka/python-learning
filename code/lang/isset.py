#!/usr/bin/env python3
"""
Проверить что существует переменная
"""
name = "bubujka"
if "name" in locals():
    print("Name defined")
else:
    print("Name not defined")

if "name2" in locals():
    print("Name2 defined")
else:
    print("Name2 not defined")

def hello():
    if "name" in locals():
        print("Name defined")
    else:
        print("Name not defined")

    if "name2" in locals():
        print("Name2 defined")
    else:
        print("Name2 not defined")

    if "name" in globals():
        print("Name defined")
    else:
        print("Name not defined")

hello()
