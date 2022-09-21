#!/usr/bin/python3

for c in range(0, 100):
    if c == 99:
        print(c)
    else:
        print('{:0>2d}'.format(c), end=", ")
