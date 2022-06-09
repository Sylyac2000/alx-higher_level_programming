#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    unique_mylist = set(my_list)
    for i in unique_mylist:
        total += i
    return(total)
