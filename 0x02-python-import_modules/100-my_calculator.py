#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    if len(argv[1:]) != 3:
        print("Usage:", argv[0], "<a> <operator> <b>")
        exit(1)

    op = argv[2]
    operators = ["+", "-", "*", "/"]
    fonctions = [add, sub, mul, div]
    if op not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    index = operators.index(op)
    fonction = fonctions[index]
    print("{:d} {:s} {:d} = {:d}".format(a, op, b, fonction(a, b)))
