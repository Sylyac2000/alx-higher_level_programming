#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nbre = 0
    for x in range(0, x):
        try:
            print("{:d}".format(my_list[x]), end="")
            nbre += 1
        except (TypeError, ValueError):
            continue
    print("")
    return nbre
