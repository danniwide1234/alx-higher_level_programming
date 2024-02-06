#!/usr/bin/python3
"""Defining a Pascal's Triangle function."""


def pascal_triangle(n):
    """Representing Pascal's Triangle of size n.

    Returning a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        x = triangles[-1]
        storage = [1]
        for k in range(len(x) - 1):
            storage.append(x[k] + x[k + 1])
        storage.append(1)
        triangles.append(storage)
    return triangles
