#!/usr/bin/python3
"""Defining a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Inserting text after each line containing a given string in a file.

    Args:
        filename (str): file name.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    t_ext = ""
    with open(filename) as f_ile:
        for line in f_ile:
            t_ext += line
            if search_string in line:
                t_ext += new_string
    with open(filename, "w") as t:
        t.write(t_ext)
