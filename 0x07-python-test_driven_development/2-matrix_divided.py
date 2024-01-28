#!/usr/bin/python3
"""

This module is consist of a function that divides the numbers of a matrix

"""


def matrix_divided(matrix, div):
    """ Function that divides the float/integer numbers of a matrix

    Args:
        matrix: list of a lists of floats/integers
        div: number which divides the matrix

    Returns:
        A new matrix with the result of the division

    Raises:
        TypeError: If the elements of the matrix aren't lists
                   If the elemetns of the lists aren't floats/integers
                   If div is not an float/integer number
                   If the lists of the matrix don't have the same size

        ZeroDivisionError: If div is zero


    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msgs_type = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msgs_type)

    len_e = 0
    msgs_size = "Each row of the matrix must have the same size"

    for item in matrix:
        if not item or not isinstance(item, list):
            raise TypeError(msgs_type)

        if len_e != 0 and len(item) != len_e:
            raise TypeError(msgs_size)

        for number in item:
            if not type(number) in (int, float):
                raise TypeError(msgs_type)

        len_e = len(item)

    f = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (f)
