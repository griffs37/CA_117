#!usr/bin/env python

import sys

def substring(word1, word2):
        if word1 in word2:
            return True
        else:
            return False

def main():
    for line in sys.stdin:
        a = line.strip().split()
        word1 = a[0].upper()
        word2 = a[1].upper()
        print(substring(word1, word2))

if __name__ == '__main__':
    main()
