#!/usr/bin/python3
"""Defining a Rectangle class."""


class Rectangle:
    """Representing a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializing a new Rectangle.

        Args:
            width (int): new rectangle width.
            height (int): new rectangle height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the Rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the Rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the Rectangle area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the Rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectan = []
        for k in range(self.__height):
            [rectan.append('#') for m in range(self.__width)]
            if k != self.__height - 1:
                rectan.append("\n")
        return ("".join(rectan))
