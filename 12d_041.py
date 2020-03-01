#!usr/bin/env python

import sys

def l2d():
	for lines in sys.stdin:
		a = lines.readlines()











def main():
    d = l2d(sys.stdin)
    for (k, v) in sorted(d.items()):
        print('{} : {}'.format(k, v))

if __name__ == '__main__':
    main()