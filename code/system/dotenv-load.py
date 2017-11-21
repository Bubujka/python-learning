#!/usr/bin/env python3
"""Считать переменные окружения из .env файла"""

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import os
print({k: v for k, v in os.environ.items() if 'MYSQL' in k})
