#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    length = len(my_list) - 1
    for n in range(length, 0):
        print("{:d}".format(n))
