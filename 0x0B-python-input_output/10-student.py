#!/usr/bin/python3
"""
Module 10-student based on 9-student.py
"""


class Student:
    """
    class Student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """  Returns dictionary description """
        if attrs is None:
            return self.__dict__
        else:
            adict = {}
            for attr in attrs:
                if attr in self.__dict__.keys():
                    adict[attr] = self.__dict__[attr]
            return adict
