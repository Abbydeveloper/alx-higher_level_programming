#!/usr/bin/python3

"""Matrix divided"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix

    Args:
    matrix: matrix provided
    div: divisor
    """

    if div == 0:
        raise ZeroDivisionError('division by zero')
    elif (not (isinstance(div, float) or isinstance(div, int))):
        raise TypeError('div must be a number')

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(elem, float) or isinstance(elem, int))
                for elem in [i for row in matrix for i in row])):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
