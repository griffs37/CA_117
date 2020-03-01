#!usr/bin/env python/

import sys

def main():
    phone_book = {}
    with open(sys.argv[1], "r") as f:
        for line in f:
            name, number, email = line.strip().split()
            phone_book[name] = number, email

    for lines in sys.stdin:
        name = lines.strip()
        if name in phone_book:
            print("Name: {}".format(name))
            print("Phone: {}".format(phone_book[name][0]))
            print("Email: {}".format(phone_book[name][1]))
        else:
            print("Name: {}".format(name))
            print("No such contact")

if __name__ == "__main__":
    main()
