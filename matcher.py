#!/usr/bin/env python

import sys

def main():
	matches = []
	try:
		with open(sys.argv[1], "r") as f:		
			newlist = f.read().splitlines()		
			list1 = newlist[0]
			list2 = newlist[1]
			line1 = list1.split()
			line2 = list2.split()
			line1 = [int(i) for i in line1]
			line2 = [int(i) for i in line2]
			#List both now in integer format
			count = 0
			for i in line1:
				if i == line2[count]:
					matches.append(line1.index(i))
				count += 1

			print(matches)
	except:
		print("Could not open {}".format(sys.argv[1]))



if __name__ == '__main__':
	main()