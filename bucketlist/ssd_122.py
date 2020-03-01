#!usr/bin/env python

import sys


def convert(n, b):
    a = []
    base_square = True
    power = 0
    while base_square:
        if n % (b ** power) == n:
            max_power = power - 1
            base_square = False
        else:
            power = power + 1

    while max_power >= 0:
        remainder = n % (b ** max_power)
        squared_digit = int((n - remainder) / b ** max_power)
        a.append(squared_digit)
        n = remainder
        max_power = max_power - 1
    return a

def square(a):
    total = 0
    for num in a:
        num = num ** 2
        total = total + num
    return total


def main():
    fail = []
    i = 1
    for line in sys.stdin:
        l = line.strip().split()
        try:
            n = int(l[0])
            b = int(l[1])
            a = convert(n, b)
            print(square(a))
        except:
            fail.append(i)
        i = i + 1
    if len(fail) > 0:
        fail = str(fail).strip("[]")
        fail = fail + " "
        print("Failed to convert line(s):", fail)


if __name__ == "__main__":
    main()
