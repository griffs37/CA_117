#!usr/bin/env python

import sys

def change(word, censored_list):
    for censored_word in censored_list:
        censored_word = censored_word.strip()
        if censored_word in word:
            return word.replace(censored_word, "@" * len(censored_word))
    return word

def main():
    censored_list = []
    with open(sys.argv[1], "r") as f:
        for line in f:
            censored_list.append(line.strip().lower())
    for line in sys.stdin:
        line = line.strip().split()
        returned = ""
        for word in line:
            returned = returned + " " + change(word, censored_list)
        print(returned.strip())

if __name__ == "__main__":
    main()
