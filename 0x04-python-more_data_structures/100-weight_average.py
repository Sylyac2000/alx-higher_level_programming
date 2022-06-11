#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    result = 0.0
    s_list = list(tuple[0] * tuple[1] for tuple in my_list)
    w_list = list(tuple[1] for tuple in my_list)
    result = sum(s_list) / sum(w_list)
    return result
