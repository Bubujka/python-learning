#!/usr/bin/env python3
"""
Осуществить POST form-data
"""
import urllib3
import json

http = urllib3.PoolManager()

r = http.request(
        'POST',
        'http://httpbin.org/post',
        fields={'name':'bubujka'})

print(r.data)
