#!/usr/bin/python3

"""LockedClass Module"""


class LockedClass:
    """Stop the user from dynamically creating new instance attributes
    unless the new instance attribute is called 'first_name'
    """
    __slots__ = ['first_name']
