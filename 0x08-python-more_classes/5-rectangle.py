#!/usr/bin/python3

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
        return self.__width * self.__height

    def perimeter(self):
        """Return the Rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rectan = []
        for h in range(self.__height):
            [rectan.append('#') for z in range(self.__width)]
            if h != self.__height - 1:
                rectan.append("\n")
        return "".join(rectan)

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        print("Bye rectangle...")

# Example script using the Rectangle class
if __name__ == "__main__":
    # Create an instance of the Rectangle class
    my_rectangle = Rectangle(width=2, height=4)

    # Access methods and properties of the rectangle
    print("Area:", my_rectangle.area())
    print("Perimeter:", my_rectangle.perimeter())

    # Print the string representation of the rectangle
    print(str(my_rectangle))

    # Print the representation of the rectangle using repr
    print(repr(my_rectangle))

    # Delete the rectangle instance
    del my_rectangle

