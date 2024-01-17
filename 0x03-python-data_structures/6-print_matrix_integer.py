#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    length = len(matrix)
    if length == 0 or matrix is None:
        return None
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end="")
            if (j < len(matrix[i]) - 1):
                    print(" ", end="")
        print("\n", end="")
