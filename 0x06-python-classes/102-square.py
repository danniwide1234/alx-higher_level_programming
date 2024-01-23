#!/usr/bin/python3
""" class Squar  defining a  square"""


class Square:
    """ class Square defining a square"""
    def __init__(self, size=0):
        """ initializing square

        Args:
            value (int): square size
        """
        self.size = size

    @property
    def size(self):
        """int: private size.

        Returns:
            Private size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets value into size, must be int.

        Args:
            value (int): size of the square.
        """
        if type(value) is not int and type(value) is not float:
            raise TypeError('size must be a number')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value  #: size of the square

    def area(self):
        """returns the area

        Returns:
            area.
        """
        return self.__size**2

    def __lt__(self, remaining):
        return self.size < remaining.size

    def __le__(self, remaining):
        return self.size <= remaining.size

    def __eq__(self, remaining):
        return self.size == remaining.size

    def __ne__(self, remaining):
        return self.size != remaining.size

    def __ge__(self, remaining):
        return self.size >= remaining.size
