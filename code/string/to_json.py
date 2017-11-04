#!/usr/bin/env python3
"""
Сериализовать массив-объект в Json
"""

import json

a = {"name": "bubujka",
     "age": 15,
     "tags": ['man', 'human'],
     'is_programmer': True}

print(json.dumps(a))


