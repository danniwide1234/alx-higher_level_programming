#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    fresh_matrix = matrix.copy()

    for m in range(len(matrix)):
        fresh_matrix[m] = list(map(lambda x: x**2, matrix[m]))

    return (fresh_matrix)
