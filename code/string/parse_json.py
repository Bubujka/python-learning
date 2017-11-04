#!/usr/bin/env python3
"""
Разобрать строку с Json
"""

import json
t = '{"name": "bubujka", "tags": ["man", "human"], "age": 15, "is_programmer": true}'
print(json.loads(t))


