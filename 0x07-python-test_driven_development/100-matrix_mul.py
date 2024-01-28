#!/usr/bin/python3
"""function that Defines a matrix multiplication ."""


def matrix_mul(m_a, m_b):
    """Multiplying two matrices.

    Args:
        m_a (list of lists of ints/floats): matrix one.
        m_b (list of lists of ints/floats): matrix two.
    Raises:
        TypeError: If either m_a or m_b is not a list of lists of ints/floats.
        TypeError: If either m_a or m_b is empty.
        TypeError: If either m_a or m_b has different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.
    Returns:
        A fresh matrix representing the multiplication of m_a by m_b.
    """

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(item, int) or isinstance(item, float))
               for item in [number for row in m_a for number in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(item, int) or isinstance(item, float))
               for item in [number for row in m_b for number in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    inverted_b = []
    for z in range(len(m_b[0])):
        fresh_row = []
        for y in range(len(m_b)):
            fresh_row.append(m_b[y][z])
        inverted_b.append(fresh_row)

    fresh_matrix = []
    for row in m_a:
        fresh_row = []
        for col in inverted_b:
            create = 0
            for k in range(len(inverted_b[0])):
                create += row[i] * col[k]
            fresh_row.append(create)
        fresh_matrix.append(fresh_row)

    return fresh_matrix
