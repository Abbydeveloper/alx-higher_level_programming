#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    keys_list = list(a_dictionary.keys())
    keys_list.sort()
    for key in keys_list:
        print("{}: {}".format(key, a_dictionary[key]))
