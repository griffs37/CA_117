#!usr/bin/env python

import sys
import math

def main():
	nums = []
	for line in sys.stdin:
		newline = line.strip("\n")
		nums.append(int(newline))
	print(nums)
	x_bar = getMean(nums)
	N = len(nums)
	total = getSum(x_bar, nums)
	print(getStandardDeviation(N, total))


def getMean(nums):
	mean = sum(nums) / len(nums)
	return mean

def getSum(x_bar, nums):
	total = []
	for x_i in nums:
		n = (x_i - x_bar) ** 2
		total.append(n)
	return sum(total)

def getStandardDeviation(N, total):
	o = total * (1 / (N - 1))
	sd = math.sqrt(o)
	return sd


if __name__ == '__main__':
	main()