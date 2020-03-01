#!/usr/bin/env python

import sys


def best(a):
    highest = 0
    tops = ""
    for people in a:
        try:
            people = people.split()
            mark = int(people[0])
            name = " ".join(people[1:])
            if mark > highest:
                highest = mark
                tops = name
            elif mark == highest:
                tops = tops + ", " + name
        except:
            print("Invalid mark {} encountered. Skipping.".format(people[0]))

    print("Best student(s):", tops)
    print("Best mark:", highest)

def main():
    try:
        with open(sys.argv[1], "r") as f:
            a = f.readlines()
            (best(a))
    except:
        print("The file" + " " + sys.argv[1] + " " + "could not be opened")

if __name__ == "__main__":
    main()
