#!usr/bin/env python

import sys

from re import findall

for line in sys.stdin:
    print(max(findall('[A-Z]+', line), key=len))
