#!/usr/bin/python3
"""Defining a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Representing a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            t = 0
            for arg in args:
                if t == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif t == 1:
                    self.size = arg
                elif t == 2:
                    self.x = arg
                elif t == 3:
                    self.y = arg
                t += 1

        elif kwargs and len(kwargs) != 0:
            for m, n in kwargs.items():
                if m == "id":
                    if n is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = n
                elif m == "size":
                    self.size = n
                elif m == "x":
                    self.x = n
                elif m == "y":
                    self.y = n

    def to_dictionary(self):
        """Returning the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
