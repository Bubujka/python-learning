#!/usr/bin/env python3
"""
Преобразовать словарь в query_string
"""

import urllib.parse

print(urllib.parse.urlencode({ 'name': 'bubujka bubujkovich=', 'age': 34}))

