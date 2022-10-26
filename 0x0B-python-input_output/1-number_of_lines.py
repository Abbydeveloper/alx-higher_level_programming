#!/usr/bin/python3
"""Module 1 - Number of lines """


def number_of_lines(filename=''):
    """Count and return the number of lines in the file filename"""

    no_of_lines = 0

    with open(filename) as f:
        text = f.readlines()
        for line in text:
            no_of_lines += 1

    return no_of_lines
