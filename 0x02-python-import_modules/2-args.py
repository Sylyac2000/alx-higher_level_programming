#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv[1:])
    arg = argv[1:]
    print("{:d} {:s}{:s}".format(length,
                                 "arguments" if (length) != 1 else "argument",
                                 "." if (length) == 0 else ":"))
    for i in range(length):
        print("{:d}: {:s}".format(i + 1, arg[i]))
