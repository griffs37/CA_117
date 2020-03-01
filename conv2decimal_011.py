#!usr/bin/env python

import sys

def convert(n, base):
    n = n[::-1]
    total = 0
    i = 0
    while i < len(n):
        total = total + ((base ** i) * int(n[i]))
        i = i + 1
    return total

def main():
    for line in sys.stdin:
        a = line.strip().split()
        n = a[0]
        base = int(a[1])
        print (convert(n, base))

if __name__ == "__main__":
   main()
