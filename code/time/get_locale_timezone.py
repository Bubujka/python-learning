#!/usr/bin/env python3
"""
Получение таймзоны, в которой мы сейчас работаем
"""
from datetime import datetime, timezone

print( datetime.now().isoformat() )

print( datetime.now(timezone.utc).isoformat() )


