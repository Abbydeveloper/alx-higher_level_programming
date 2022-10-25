#!/usr/bin/python3

"""Module 1-my_list
Create a class to inherit from the list class
"""


class MyList(list):
    """Implement sorting for lists."""

    def print_sorted(self):
        """Sort  a list in ascending order and print"""
        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
