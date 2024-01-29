#!/usr/bin/python3
"""Defining a Rectangle class."""


class Rectangle:
    """Representing a rectangle.

    Attributes:
        number_of_instances (int): Rectangle instances number.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializing a new Rectangle.

        Args:
            width (int): The new rectangle width.
            height (int): The new rectangle height.
        """
        type(self).number_of_instances += 1
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
        """Return the Rectangle perimieter."""
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
        for f in range(self.__height):
            [rectan.append('#') for n in range(self.__width)]
            if f != self.__height - 1:
                rectan.append("\n")
        return ("".join(rectan))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rectan = "Rectangle(" + str(self.__width)
        rectan += ", " + str(self.__height) + ")"
        return (rectan)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
