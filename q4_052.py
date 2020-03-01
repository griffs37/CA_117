#!usr/bin/env python

import sys

foods = open(sys.argv[1])

d = {}
for line in foods:
    tokens = line.split()
    d[tokens[0]] = (tokens[1])

people = {}

for line in sys.stdin:
    name = line.split(",")[0]
    food = line.split(",")[1:]
    total = 0
    for f in food:
        if f in d:
            total += d[f]
        else:
            total += 100
    people[name] = total


pwidth = max(d.keys(), key=len)
nwidth = max(d.values(), key=len)
for k, v in people.items():
    print("{:{}} : {:{}}".format(k, pwidth, v, nwidth))