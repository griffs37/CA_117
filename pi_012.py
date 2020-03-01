#!/usr/bin/env python

import sys

import math

def main():
    s = sys.argv
    n = s[1]
    print('{:.{}f}'.format(math.pi, n))


if __name__ == "__main__":
    main()
