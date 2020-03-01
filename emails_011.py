#!/usr/bin/env python

import sys

def main():
    for line in sys.stdin:
        a = line.strip().split("@")[0]
        a = a.split()
        i = 0
        nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        a = a[0]
        for char in nums:
            if char in a:
                a = a.replace(char, "")
        a = a.title().split(".")
        print(a[0], a[1])

if __name__ == "__main__":
    main()
