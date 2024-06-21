#!/usr/bin/python3

"""Module to append to a file"""


def append_write(filename="", text=""):
    """Function appends a string to the end of a text file and
    returns the number of characters added"""

    with open(filename, mode="a") as f:
        return f.write(text)
