#!/usr/bin/env python3
"""
Экранирование html
"""

import html
name = '<b id="zuzujka">bubujka</b>'
print(html.escape(name))
print(html.unescape(html.escape(name)))

