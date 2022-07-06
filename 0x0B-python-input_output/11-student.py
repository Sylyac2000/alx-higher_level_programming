#!/usr/bin/python3
"""
Module 11-student based  (based on 10-student.py)
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

    def reload_from_json(self, json):
        """
        replaces all attributes
        """
        for key, value in json.items():
            setattr(self, key, value)
