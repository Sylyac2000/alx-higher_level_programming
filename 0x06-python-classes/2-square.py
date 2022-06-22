#!/usr/bin/python3
"""
This module is about 2-square
Write a class Square that defines a square by: (based on 1-square.py)
"""


class Square:
    """
    class Square definition

    Args:
        size : size of a side in square
    """
    def __init__(self, size=0):
        """
        Initializes square

        Attributes:
            size (int): the size of a side of square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
