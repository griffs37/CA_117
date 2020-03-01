#!usr/bin/env python

import sys

d = { "January" : "1",
	  "February" : "2",
	  "March" : "3",
	  "April" : "4",
	  "May" : "5",
	  "June" : "6",
	  "July" : "7",
	  "August" : "8",
	  "September" : "9",
	  "October" : "10",
	  "November" : "11",
	  "December" : "12"
}

def main():
	for line in sys.stdin:
		newline = line.strip().split()
		day = newline[0]
		month = newline[1]
		year = newline[2]
		return "{}/{}/{}".format(day, d[month], year[2:])

if __name__ == '__main__':
	main()