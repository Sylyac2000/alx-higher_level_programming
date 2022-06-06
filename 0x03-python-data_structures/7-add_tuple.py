def add_tuple(tuple_a=(), tuple_b=()):

    len_a = len(tuple_a)
    len_b = len(tuple_b)
    sum_a_0 = (tuple_a[0] if len_a > 0 else 0)
    sum_b_0 = (tuple_b[0] if len_b > 0 else 0)
    sum_0 = sum_a_0 + sum_b_0

    sum_a_1 = (tuple_a[1] if len_a > 1 else 0)
    sum_b_1 = (tuple_b[1] if len_b > 1 else 0)
    sum_1 = sum_a_1 + sum_b_1
    sums = (sum_0, sum_1)
    return sums
