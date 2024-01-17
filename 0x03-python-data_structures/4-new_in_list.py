#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    length = len(my_list)
    if idx > length:
        return my_list
    new_list = []
    for n in range(0, length + 1):
        if n == idx:
            new_list[n] = element
        else:
            new_list[n] = my_list[n]

    return new_list
