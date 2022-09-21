#!/usr/bin/python3

for c in range(ord('a'), ord('z') + 1):
    if c != 'q' and c != 'e':
        print("{:c}".format(c), end="")
