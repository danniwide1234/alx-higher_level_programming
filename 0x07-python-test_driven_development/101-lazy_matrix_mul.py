#!/usr/bin/python3
"""Defining  a matrix multiplication function using NumPy."""
import numpy as mp


def lazy_matrix_mul(m_a, m_b):
    """Returning the multiplication of two matrices.

    Args:
        m_a (list of lists of ints/floats): matrix one.
        m_b (list of lists of ints/floats): matrix two.
    """

    return (mp.matmul(m_a, m_b))
