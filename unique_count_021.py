#!usr/bin/env python

import sys
import string

def main():
    f = sys.stdin.read()
    f = f.lower()
    answer = ""
    answer = ''.join(c for c in f if c not in string.punctuation).split()
    input = set(answer)
    print(len(input))

if __name__ == "__main__":
    main()
