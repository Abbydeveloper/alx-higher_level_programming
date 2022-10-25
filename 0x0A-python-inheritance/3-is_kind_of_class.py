#!/usr/bin/python3

"""Module 3 - Is kind of class"""


def is_kind_of_class(obj, a_class):
    """Check if object obj is an instance of the class a_class or any of its
    children
    """

    return isinstance(obj, a_class)
