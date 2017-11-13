#!/usr/bin/env python3
"""
Basic авторизация у HTTP-запросов
"""

import urllib3

http = urllib3.PoolManager()
headers = urllib3.util.make_headers(basic_auth='helo:wrld')
r = http.request('GET', 'http://httpbin.org/basic-auth/helo/wrld', headers=headers)
print(r.status, r.data)






