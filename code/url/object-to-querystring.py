#!/usr/bin/env python3
"""Превратить словарь в query-string"""

import urllib.parse
print(urllib.parse.urlencode({'name': 'zuzujka'}))
