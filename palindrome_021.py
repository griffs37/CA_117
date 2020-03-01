#!usr/bin/env python

import sys

def palin(rev):
   i = 0
   while i < len(rev) / 2:
      if rev[i] != rev[-(i + 1)]:
         return False
      i = i + 1
   
   return True

def main():
   for line in sys.stdin:
      rev = []
      rev = line.lower()
   for i in rev:
      if i.isalpha() == False:
         rev = rev.replace(i, "")
 
   print(palin(rev))

if __name__ == "__main__":
   main()