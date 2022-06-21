#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_res = []
    for x in range(list_length):
        res = 0
        try:
            res = my_list_1[x] / my_list_2[x]
        except (ZeroDivisionError, ValueError):
            print("division by 0")
        except (TypeError):
            print("wrong type")
        except (IndexError):
            print("out of range")
        finally:
            list_res.append(res)
    return list_res
