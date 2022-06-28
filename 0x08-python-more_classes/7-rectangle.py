#!/usr/bin/python3
"""
This module is about 6-rectangle
Write a class Rectangle that defines a rectangle by: (based on 5-rectangle.py)
"""


class Rectangle:
    """Defines class rectangle with private attribute width and height
     Args:
        width (int): width
        height (int): height
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialize rectangles """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ Getter returns width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter sets width if int > 0 """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter returns height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter sets height if int > 0 """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Return width * height """
        return self.__width * self.__height

    def perimeter(self):
        """ Return 2*width + 2*height (or return 0 if width or height is 0)"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.height)

    def __str__(self):
        """ Prints rectangle with # """
        if self.__width == 0 or self.__height == 0:
            return ""
        img = "\n".join([str(self.print_symbol) * self.__width
                         for rows in range(self.__height)])
        return img

    def __repr__(self):
        """ String representation to be able to recreate a new instance"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ Delete instance of class Rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
