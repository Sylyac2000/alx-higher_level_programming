#!/usr/bin/python3
"""
This module is about 4-square
Write a class Square that defines a square by: (based on 1-square.py)
"""


class Square:
    """
    class Square definition

    Attributes:
        size : size of a side in square
    """
    def __init__(self, size=0):
        """
        Initializes square

        Attributes:
            size (int): the size of a side of square
        """
        self.__size = size

    @property
    def size(self):
        """"
        Getter

        Return: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter

        Args:
            value: sets size to value, if int and >= 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates area of square

        Returns:
            area
        """
        return (self.__size)**2
