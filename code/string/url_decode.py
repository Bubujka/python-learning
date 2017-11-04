#!/usr/bin/env python3
"""
Разэкранировать URL
"""

import urllib.parse

t = "%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82%3D%D0%BA%D0%B0%D0%BA%22%D0%B4%D0%B5%D0%BB%D0%B0%3F"

print(urllib.parse.unquote(t))


