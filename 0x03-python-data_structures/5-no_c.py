#!/usr/bin/python3

def no_c(my_string):
    length = len(my_string)
    new_string = ""
    for n in range(0, length):
        if (my_string[n] != 'c' and my_string[n] != 'C'):
            new_string += my_string[n]

    return new_string
