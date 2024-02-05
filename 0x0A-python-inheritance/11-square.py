#!/usr/bin/python3
# -*- coding: utf-8 -*-


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """
    A Square class shape, inherit from BaseGeometry
    """
    def __init__(self, size):
        """"
        Initialising function for Square

        Attributes:
            size (int): the square size
        """
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        str funtion to print with/height

        Returns:
            Return width/height
        """
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)

    def area(self):
        """
        A function that calculates the Square area
        """
        return self.__size ** 2
