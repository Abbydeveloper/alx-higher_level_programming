#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    length = len(my_list)

    is_divisible = []
    for n in range(0, length):
        if my_list[n] % 2 == 0:
            is_divisible.append(True)
        else:
            is_divisible.append(False)
    return is_divisible
