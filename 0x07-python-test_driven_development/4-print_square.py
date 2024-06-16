#!/usr/bin/python3

"""Define a function to print a square"""


def print_square(size):
    """
    Print a square with the character #

    Args:
    size (int): the size length of the square
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        if isinstance(size, float):
            raise TypeError('size must be an integer')
        raise ValueError('size must be >= 0')

    for i in range(size):
        for j in range(size):
            print('#', end="")
        print("")
