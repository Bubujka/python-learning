#!/usr/bin/env python3
"""
Разбор-сериализация даты в iso8601
"""

from datetime import datetime
import time

print(time.time())
print(datetime.now().timestamp())
print(datetime.now().isoformat())
print(datetime.fromtimestamp(3600*24).isoformat())

