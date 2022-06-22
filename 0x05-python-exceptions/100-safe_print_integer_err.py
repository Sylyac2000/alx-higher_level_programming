#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    bool = False
    try:
        print("{:d}".format(value))
        bool = True
    except (TypeError, ValueError) as err:
        print("Exception: {}\n".format(err), file=sys.stderr)
    return bool
