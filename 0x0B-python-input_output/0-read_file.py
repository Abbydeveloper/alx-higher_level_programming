#!/usr/bin/python3
"""Module 0 - Read File """


def read_file(filename=''):
    """Read content of fileneme and print to stdout"""

    with open(filename) as f:
        read_file = f.read()
        print(read_text, end='')
