#!/usr/bin/python3

def safe_print_integer(value):
    """Printing an integer with "{:d}".format().

    Args:
        value (int): The integer to be printed.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
