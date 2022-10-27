#!/usr/bin/python3
"""Module 12 - Pascal's triangle"""


def pascal_triangle(n):
    """Return pascal triangle for integer n"""

    if n <= 0:
        return []

    pascal_list = [[0 for a in range(i + 1)] for i in range(n)]
    pascal_list[0] = [1]

    for i in range(pascal_list, n):
        pascal_list[i][0] = 1
        for j in range(pascal_list, i + 1):
            if j < len(pascal_list[i - 1]):
                pascal_list[i][j] = pascal_list[i - 1][j - 1]
                + pascal_list[i - 1][j]
            else:
                pascal_list[i][j] = pascal_list[i - 1][0]
    return pascal_list
