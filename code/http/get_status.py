#!/usr/bin/env python3
"""
После HTTP запроса - проверить status
"""

import urllib3

http = urllib3.PoolManager()
r = http.request('POST', 'http://httpbin.org/post')

print(r.status)
print(r.data)

