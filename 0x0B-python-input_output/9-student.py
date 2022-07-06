#!/usr/bin/python3
"""
This module is about 2-square
Write a class Square that defines a square by: (based on 1-square.py)
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

    def to_json(self):
        """  Returns dictionary description """
        return self.__dict__
