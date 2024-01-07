#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for y in range(len(matrix)):
        for z in range(len(matrix[y])):
            if z != 0:
                print(" ", end='')
            print("{:d}".format(matrix[y][z]), end='')
        print()
