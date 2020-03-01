#!/usr/bin/env python

import sys

def middle(s):
    return s[len(s) // 2]

def main():
    for line in sys.stdin:
        if len(line) % 2 == 0:
            newline = middle(line.strip())
            if newline:
                print(newline)
        else:
            print("No middle character!")

if __name__ == "__main__":
    main()