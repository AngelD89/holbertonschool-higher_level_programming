#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def main():
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a_str, op, b_str = sys.argv[1], sys.argv[2], sys.argv[3]
    ops = {"+": add, "-": sub, "*": mul, "/": div}

    if op not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(a_str)
    b = int(b_str)
    result = ops[op](a, b)
    print("{} {} {} = {}".format(a, op, b, result))


if __name__ == "__main__":
    main()
