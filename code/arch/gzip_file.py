#!/usr/bin/env python3
"""Заархивировать строку"""

import gzip
with open('_tmp/res.txt.gz', 'wb') as f:
    f.write( gzip.compress("Heeeeeeeeeeeeelo world".encode('utf-8')) )

