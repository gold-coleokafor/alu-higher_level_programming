#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    argv = sys.argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if argv[2] not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(argv[1])
    b = int(argv[3])
    print("{} {} {} = {}".format(a, argv[2], b, ops[argv[2]](a, b)))
