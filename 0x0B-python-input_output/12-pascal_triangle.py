#!/usr/bin/python3
"""
Module 12-pascal_triangle

function that returns int lists of pascal triangle
"""


def pascal_triangle(n):
    """
    returns int lists of pascal triangle
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    triangledepascal = [[1]]
    for rows in range(n-1):
        myl = [1]
        for i in range(rows):
            myl.append(triangledepascal[-1][i] + triangledepascal[-1][i+1])
        myl.append(1)
        triangledepascal.append(myl)
    return triangledepascal
