#!/usr/bin/env python

import sys

def chop(s):
    return s[1:len(s) - 1]

def main():
    for line in sys.stdin:
        newline = chop(line.strip())
        if newline:
            print(newline)




if __name__ == "__main__":
    main()