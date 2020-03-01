#!usr/bin/env python

import sys

from string import punctuation as punc

def main():
    dictionary = {}
    words = [w.strip().lower().rstrip(punc) for w in sys.stdin.read().split()]
    a = []
    for i in words:
        if i in dictionary:
            dictionary[i] += 1
        else:
            a.append(i)
            a = sorted(a)
            dictionary[i] = 1

    for i in a:
        if len(i) > 3 and dictionary[i] > 2:
            print("{:>{:d}s}".format(i, 9), ":", "{:{:d}d}".format(dictionary[i], 2))
            #print(i, ":", dictionary[i])

if __name__ == "__main__":
    main()
