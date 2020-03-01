#!/usr/bin/env python

import sys

def password(line):
        upper = 0
        digit = 0
        lower = 0
        special = 0
        i = 0
        while i < len(line):
            if line[i].isupper():
                upper = 1
            elif line[i].isdigit():
                digit = 1
            elif line[i].islower():
                lower = 1
            else:
                special = 1
            i = i + 1
        total = upper + digit + lower + special
        return total

def main():
    for line in sys.stdin:
        s = line.strip()
        print(password(s))



if __name__ == "__main__":
    main()