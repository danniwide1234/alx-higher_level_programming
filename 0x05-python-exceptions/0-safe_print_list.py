#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.

    Args:
        my_list (list): list printing elements from.
        x (int): elements number of my_list to print.

    Returns:
        elements number to printed.
    """
    pin = 0
    for k in range(x):
        try:
            print("{}".format(my_list[k]), end="")
            pin += 1
        except IndexError:
            break
    print("")
    return (pin)
