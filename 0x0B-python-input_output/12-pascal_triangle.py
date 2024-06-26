#!/usr/bin/python3

"""12-pascal_trianle.py"""


def pascal_triangle(n):
    """Return a list of lists of integers representing the pascal's
    triangle of n"""

    n_list = []

    if n <= 0:
        return n_list

    n_list = [[1]]

    for x in range(1, n):
        row = [1]
        for y in range(1, x):
            row.append(n_list[x-1][y-1] + n_list[x-1][y])
        row.append(1)
        n_list.append(row)
    return n_list
