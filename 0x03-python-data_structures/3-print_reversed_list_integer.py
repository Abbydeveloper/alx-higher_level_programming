#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if (my_list is None or len(my_list) == 0):
        return ''
    length = len(my_list) - 1
    for n in range(-1, -length):
        print("{:d}".format(my_list[n]))
