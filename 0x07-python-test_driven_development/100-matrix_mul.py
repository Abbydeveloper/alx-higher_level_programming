#!/usr/bin/python3

"""Matris Multiplication Module"""


def matrix_mul(m_a, m_b):
    """function that multiples 2 matrices

    Args:
    m_a (list of lists): first matrix
    m_b (list of lists): second matrix
    """

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_a must be a list')

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError('m_a must be a list of lists')
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError('m_b must be a list of lists')

    if not all((isinstance(elem, int) or isinstance(elem, float))
                for elem in [x for row in m_a for x in row]):
        raise TypeError('m_a should contain only integers or floats')
    if not all((isinstance(elem, int) or isinstance(elem, float))
            for elem in [y for row in m_b for y in row]):
        raise TypeError('m_b should contain only integers or floats')

    if (len(m_a[0]) != len(m_b)):
        raise Valueerror("m_a and m_b can't be multiplied")

    if (not all(len(row) == len(m_a[0]) for row in m_a)):
        raise TypeError('each row of m_a must be of the same size')
    if (not all(len(row) == len(m_b[0]) for row in m_b)):
        raise TypeError('each row of m_b must be of the same size')

    new_matrix = []
    for row in m_a:
        new_row = []
        for i in range(len(row)):
            prod = 0
            for j in range(len(m_b)):
                prod += row[j] * m_b[j][i]
            new_row.append(prod)
        new_matrix.append(new_row)

    return (new_matrix)

