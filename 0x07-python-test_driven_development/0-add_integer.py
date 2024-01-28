#!/usr/bin/python3
"""

This module consist a function that adds two numbers

"""


def add_integer(a, b=98):
    """ Function adding two integer and/or float numbers

    Args:
        a:  number one
        b:  number two

    Returns:
        addition of the two given numbers

    Raises:
        TypeError: If a or b aren't float numbers and/or integers

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
