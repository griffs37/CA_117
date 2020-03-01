#!usr/bin/env python

import sys

def main():
    a = []
    for line in sys.stdin:
        w = line.lower().strip()
        if "qu" in w:
            w = w.replace("qu", "")
        if "q" in w:
            a.append(line.strip())
    print("Words with q but no u:", a)

if __name__ == "__main__":
    main()
