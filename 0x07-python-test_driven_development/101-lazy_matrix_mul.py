#!/usr/bin/python3
"""Defines a module for multiplying two matrices using NumPy"""

import numpy


def lazy_matrix_mul(m_a, m_b):
    """Multiply 2 matrices using the NumPy function


    Args:
    m_a (list of lists of integers/floats): first matrix
    m_b (list of lists of integers/floats): second matrix
    """

    return (numpy.matmul(m_a, m_b))
