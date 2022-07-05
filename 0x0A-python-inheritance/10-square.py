#!/usr/bin/python3
"""
Module 10-Square inherits from Rectangle (7-base_geometry.py).

"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from Rectangle, who inherits from BaseGeometry"""
    def __init__(self, size):
        """initializes """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
