#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div


def main():
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a_str, op, b_str = argv[1], argv[2], argv[3]
    ops = {"+": add, "-": sub, "*": mul, "/": div}

    if op not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(a_str)
    b = int(b_str)
    result = ops[op](a, b)
    print("{} {} {} = {}".format(a, op, b, result))


if __name__ == "__main__":
    main()
