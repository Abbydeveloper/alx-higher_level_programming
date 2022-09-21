#!/usr/bin/python3

for c in range(ord('z'), ord('a')-1, -1):
    if c % 2 == 0:
        print('{:c}{:s}'.format(c, chr(c), end=''))
    else:
        print('{:c}{:s}'.format(c, chr(c - 33), end=''))
