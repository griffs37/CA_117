#! usr/bin/env python

import sys

def capitals(s):
    first = s[0]
    last = s[-1]
    return first.capitalize() + s[1:-1] + last.capitalize()


def main():
    for line in sys.stdin:
        if len(line) >= 3:
            newline = capitals(line.strip())
            if newline:
                print(newline)

if __name__ == "__main__":
    main()