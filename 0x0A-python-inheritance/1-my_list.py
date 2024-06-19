#!/usr/bin/python3

"""MyList Module"""


class MyList(list):
    """MyList inherits from list class"""

    def ___init___(self):
        """Initialixe the MyList class"""
        super().__init__()

    def print_sorted(self):
        """print the list, but sorted in ascending order"""
        print(sorted(self))
