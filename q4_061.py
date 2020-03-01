#!usr/bin/env python

import sys

from re import findall

print(max(findall(r'[A-Z]+', s), key=len))
