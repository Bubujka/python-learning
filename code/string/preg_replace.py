#!/usr/bin/env python3
"""
Замена по регулярному выражению
"""

import re

s = "my name is: Bubujka. Age: 28"

print(re.sub(': (.*)\.', r"!!!\1!!!", s))
print(s)
