#!usr/bin/env python
    
import sys

new_dictionary = {}

def swap_keys_values(d):
    new_dictionary = dict([(v,k) for k,v in d.items()])
    return new_dictionary
