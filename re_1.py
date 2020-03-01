#!usr/bin/env python

import sys

from re import findall

vt = "3.62pm, 13.12.pm, 5.5am, 04.12pm, a3.32am"

ans = findall(r'(?:[1-9]|1[0-2])[.:]\d\d[ap]m', vt)

print(ans)