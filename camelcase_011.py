#!/usr/bin/env python

import sys

def main():
    for line in sys.stdin:
        a = line.strip().split()
        i = 0
        while i < len(a):
            a[i] = a[i].title()
            i += 1
        b = ' '.join(map(str, a))
        print(b)

if __name__ == "__main__":
    main()
