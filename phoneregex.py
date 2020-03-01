#!/usr/bin/env python

from re import findall

nums = open("phonenums.txt")

s = nums.read()

phonetest = r"\b(?:085|086|087)(?:[-\s]|)\d{7}\b"

print(findall(phonetest, s))