#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_sum = 0
    new_list = []

    for elem in my_list:
        if elem not in new_list:
            uniq_sum += elem
            new_list.append(elem)
    return (uniq_sum)
