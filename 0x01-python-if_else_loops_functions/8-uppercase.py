#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase."""
    for t in str:
        if ord(t) >= 97 and ord(t) <= 122:
            t = chr(ord(t) - 32)
        print("{}".format(t), end="")
    print("")
