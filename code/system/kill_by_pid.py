#!/usr/bin/env python3
"""
Убить процесс по pid
"""
import sys
import os
import signal
id=int(sys.argv[1])

os.kill(id, signal.SIGTERM)


