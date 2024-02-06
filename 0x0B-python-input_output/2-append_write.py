#!/usr/bin/python3
"""Defining a file-appending function."""


def append_write(filename="", text=""):
    """Appending a string to the end of a UTF8 text file.

    Args:
        filename (str): file name to be appended.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as t:
        return t.write(text)
