#!/usr/bin/python3
"""Function that Defines a text-indentation."""


def text_indentation(text):
    """Printing text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to be printed.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    n = 0
    while n < len(text) and text[n] == ' ':
        n += 1

    while n < len(text):
        print(text[n], end="")
        if text[n] == "\n" or text[n] in ".?:":
            if text[n] in ".?:":
                print("\n")
            n += 1
            while n < len(text) and text[n] == ' ':
                n += 1
            continue
        n += 1
