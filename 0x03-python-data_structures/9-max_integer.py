#!/usr/bin/python3

def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return None
    a = 0
    for n in range(0, length):
        if my_list[n] > a:
            a = my_list[n]
    return a
