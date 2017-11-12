#!/usr/bin/env python3
"""
Осуществить POST со своим body (json)
"""

import urllib.request
import json
import common

common.urlopen(urllib.request.Request(
    'https://httpbin.org/post',
    data=json.dumps({'name': 'bubujka', 'age': 32}).encode('utf-8'),
    headers={'x-whom': 'Its me!', 'content-type': 'application/json'},
    method='POST'))


