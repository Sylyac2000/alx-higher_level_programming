#!/usr/bin/python3
"""
This module is about 1-square
Write a class Square that defines a square by: (based on 0-square.py)
"""


class Square:
    """
    class Square definition

    Args:
        size : size of a side in square
    """
    def __init__(self, size):
        """
        Initializes square

        Attributes:
            size: the size of a side of square
        """
        self.__size = size
