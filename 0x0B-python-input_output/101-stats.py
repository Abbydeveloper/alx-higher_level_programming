#!/usr/bin/python3
"""Module 14 - Log Parsing"""


import sys


status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
stat = {}
count = 0

try:
    for line in sys.stdin:
        if count == 10:
            print_stats(size, stat)
            count = 1
        else:
            count += 1


            line = line.split()

            try: 
                size += int(line[-1])
            except(IndexError, ValueError):
                pass


            try:
                if line[-2] in status_codes:
                    if stat.get(line[-2], -1) == -1:
                        stat[line[-2]] = 1
                    else:
                        stat[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, stat)

    except KeyboardInterupt:
        print_stats(size, stat)
        raise

def print_stats(size, stat):
    """Print statistics"""
    print("File size: {}".format(size))
    for key in sorted(stat):
        print("{}: {}".format(key, stat[key]))




