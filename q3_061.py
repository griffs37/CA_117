#!usr/bin/env python

import sys

def main():
	for password in sys.stdin:
		total = 0
		uppers = 0
		lowers = 0
		digits = 0
		others = 0
		for c in password:
			if c.isupper():
				uppers = 1
			if c.islower():
				lowers = 1
			if c.isdigit():
				digits = 1
			else:
				others = 1
			total = lowers + uppers + digits + others
		print(total)

if __name__ == '__main__':
	main()
