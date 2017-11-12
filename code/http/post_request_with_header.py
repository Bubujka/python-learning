#!/usr/bin/env python3
"""
Осуществить POST запрос с передачей своих заголовков
"""

import urllib.request
import common

common.urlopen(urllib.request.Request(
    'https://httpbin.org/post',
    headers={'x-whom': 'Its me!'},
    method='POST'))


