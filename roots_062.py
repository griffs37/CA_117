#!usr/bin/env python

import sys

def do_roots(a, b, c):
    dis = b ** 2 - (4 * a * c)
    if dis < 0:
        return None
    r1 = (-b + dis ** 0.5) / (2 * a)
    r2 = (-b - dis ** 0.5) / (2 * a)
    return r1, r2

for line in sys.stdin:
    a, b, c = map(int, line.split())
    roots = do_roots(a, b, c)

    if roots is None:
        print(None)
    else:
        print('r1 = {}, r2 = {}'.format(*roots))
