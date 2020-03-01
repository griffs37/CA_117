#!usr/bin/env python

import sys

from re import findall

for line in sys.stdin:
    print(max(re.findall('[A-Z]+', line), key=len))
