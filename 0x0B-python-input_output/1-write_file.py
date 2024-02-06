#!/usr/bin/python3
"""Defining a file-writing function."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): file name to be written.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as m:
        return m.write(text)
