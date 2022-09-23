#!/usr/bin/python3
"""
Write a function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):

	thelist = list_of_integers
	if len(thelist) == 0:
        return None

    debut = 0
    fin = len(thelist)-1

    if thelist[debut] > thelist[debut+1]:
        return thelist[debut]
    if thelist[fin] > thelist[fin-1]:
        return thelist[fin]

    mid = (debut+fin)//2
    if thelist[mid-1] < thelist[mid] and thelist[mid+1] < thelist[mid]:
        return thelist[mid]
    if thelist[mid] < thelist[mid-1]:
        return find_peak(thelist[debut:mid+1])
    elif thelist[mid] < thelist[mid+1]:
        return find_peak(l[mid:fin+1])
    else:
        return thelist[debut]
