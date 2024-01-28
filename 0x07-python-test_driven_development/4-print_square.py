#!/usr/bin/python3
"""function that Defines a square-printing."""


def print_square(size):
    """Printing a square with the # character.

    Args:
        size (int): The width/height of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for k in range(size):
        [print("#", end="") for m in range(size)]
        print("")
