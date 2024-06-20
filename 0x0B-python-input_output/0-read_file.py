#!/usr/bin/python3
"""Read File Module"""


def read_file(filename=""):
    """Read a text file and print it to stdout"""

    with open(filename) as f:
        read_data = f.read()
        print(read_data, end="")
