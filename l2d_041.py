#!usr/bin/env python


dictionary = {}

def l2d(file):
    list1 = []
    for line in file:
        line = line.strip().split()
        list1.append(line)
    animals = list1[0]
    nums = list1[1]
    dictionary = dict(zip(animals, nums))
    return dictionary
