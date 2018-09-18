#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print()
    for row in matrix:
        for i in row:
            print("{:d}".format(i), end='')
            if i != row[-1]:
                print(' ', end='')
        print()
