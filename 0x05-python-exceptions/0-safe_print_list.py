#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nbre = 0
    for x in range(0, x):
        try:
            print(my_list[x], end="")
            nbre += 1
        except Exception:
            pass
    print("")
    return nbre
