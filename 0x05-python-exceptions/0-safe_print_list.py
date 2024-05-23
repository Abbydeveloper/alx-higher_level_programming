#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    no_elem = 0

    for i in range(x):
        try:
            print('{}'.format(my_list[i]), end='')
            no_elem += 1
        except IndexError:
            break
    print('')
    return (no_elem)

