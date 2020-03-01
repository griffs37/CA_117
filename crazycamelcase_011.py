#!/usr/bin/env python

import sys

def capitalise(s):
    s, result = s, ""
    for word in s.split():
        result += word[:-1] + word[-1].upper() + " "
    return result[:-1]

def main():
    for line in sys.stdin:
        s = line
        print(capitalise(line))

if __name__ == "__main__":
    main()
