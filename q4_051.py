#!usr/bin/env python

import sys

mean = 0
median = 0

def avg(n):
    return sum(n) / len(n)

def mid(n):
    if len(n) % 2 == 0:
        return (n[int(len(n) / 2)] + n[int(len(n) / 2 - 1)]) / 2
    else:
        return n[int(len(n) / 2)]

def main():
    nums = sorted([float(n.strip("\n")) for n in sys.stdin])
    mean = avg(nums)
    median = mid(nums)
    print("Mean: {:.1f}".format(mean))
    print("Median: {:.1f}".format(median))

if __name__ == "__main__":
    main()
