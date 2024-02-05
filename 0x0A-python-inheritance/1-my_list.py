#!/usr/bin/python3
"""MyList that inherits from list as class
"""


class MyList(list):
    """inherits from list"""
    def print_sorted(self):
        """prints the list, but sorted
        (ascending sort)
        """
        print(sorted(self))
