#!/usr/bin/env python3
"""
Получить информацию из заголовков ответа
"""

import urllib3

http = urllib3.PoolManager()
r = http.request('GET', 'http://httpbin.org/get')
print(r.headers)


