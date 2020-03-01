#!usr/bin/env python

import sys

def tokens(a):
   totals = 0
   for word in a:
      b = word.split()
      totals = totals + len(b)
   return totals

def main():
   a = sys.stdin.readlines()
   print(tokens(a))

if __name__ == "__main__":
   main()
