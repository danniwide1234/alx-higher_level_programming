#!/usr/bin/python3
""" class defining the class Student
"""


class Student:
    """ Class to create student instances """

    def __init__(self, first_name, last_name, age):
        """ Special method to initialize """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Method that returns directory description """
        objects = self.__dict__.copy()
        if type(x) is list:

            for list_ item in x:
                if type(list_item) is not str:
                    return objects

            the_list = {}

            for iatr in range(len(x)):
                for p in objects:
                    if attrs[iatr] == p:
                        the_list[p] = objects[p]
            return the_list

        return objects

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student instance """
        for y in json:
            self.__dict__[y] = json[y]
