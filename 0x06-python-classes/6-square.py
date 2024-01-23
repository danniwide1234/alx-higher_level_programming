#!/usr/bin/python3
"""Defining a class Square."""


class Square:
    """Representing a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing a new square.

        Args:
            size (int): new square size.
            position (int, int): new square position.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(measure, int) for measure in value) or
                not all(measure >= 0 for measure in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returning the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Printing the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for t in range(0, self.__position[1])]
        for t in range(0, self.__size):
            [print(" ", end="") for a in range(0, self.__position[0])]
            [print("#", end="") for b in range(0, self.__size)]
            print("")
