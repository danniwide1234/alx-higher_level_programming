#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda p: list(map(lambda q: q**2, p)), matrix)))
