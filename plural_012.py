#!/usr/bin/env python

import sys

def plural(s):
    noun = ["ch", "sh", "x", "s", "z"]
    vowel = ["a", "o", "i", "e", "u"]
    f = ["f", "fe"]
    o = ["o"]
    if s[len(s) - 2:] in noun:
        s = s + "es"
    elif s[len(s) - 1] in noun:
        s = s + "es"
    elif s[len(s) - 2] not in vowel and s[len(s) - 1] == "y":
        s = s[:len(s) - 1] + "ies"
    elif s[len(s) - 2:len(s) - 1] in f:
        s = s[:len(s) - 2] + "ves"
    elif s[len(s) - 1] in f:
        s = s[:len(s) - 1] + "ves"
    elif s[len(s) - 1] in o:
        s = s + "es"
    else:
        s = s + "s"
    return s

def main():
    for line in sys.stdin:
        s = line.strip()
        print(plural(s))



if __name__ == "__main__":
    main()

