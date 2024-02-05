#!/usr/bin/python3
""" Defining a base geometry class BaseGeometry
"""


class BaseGeometry:
    """ empty class"""
    def area(self):
        raise Exception('area() is not implemented')
