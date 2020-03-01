#!usr/bin/env python

import sys

def main():
    for word in sys.stdin:
        word = word.strip()
        new_word = word.lower()
        for c in word.lower():
            if c not in "aeiou":
                new_word = new_word.replace(c, "", 1)
        if new_word == "aeiou":
            print(word)

if __name__ == "__main__":
    main()
