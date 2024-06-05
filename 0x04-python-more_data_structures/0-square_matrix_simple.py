#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    new_list = []

    for column in matrix:
        result = [x**2 for x in column]
        new_list.append(result)
    return (new_list)
