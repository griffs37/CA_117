#!usr/bin/env python

def build_dictionary(filename):
    d = {}
    for line in open(filename):
        tokens = line.split()
        d[tokens[0]] = int(tokens[1])
    return d


def extract_range(d, low, high):
    new_dict = {}
    for k, v in d.items():
        if low <= v and v <= high:
            new_dict[k] = v
    return new_dict
