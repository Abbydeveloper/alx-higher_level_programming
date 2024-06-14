#!/usr/bin/python3

"""Define a function to add integers"""


def add_integer(a, b=98):
    """
    Function to add two numbers

    Floating numbers are typecasted to integers before addition

    Args:
    a (int): first number to add
    b (int): second number to add

    Raises:
    TypeError: if either args are not floating numbers or integers
    """
    if not ((isinstance(a, int) or isinstance(a, float))):
        raise TypeError('a must be an integer')
    if not ((isinstance(b, int) or isinstance(b, float))):
        raise TypeError('b must be an integer')
    return (int(a) + int(b))
