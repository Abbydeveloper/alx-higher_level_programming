#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if (len(sys.argv) != 4):
        print(len(sys.argv))
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operators = ["+", "-", "*", "/"]
    operator = sys.argv[2]

    if (operator not in operators):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    result = 0

    if (operator == '+'):
        result = add(a, b)
    if (operator == '-'):
        result = sub(a, b)
    if (operator == '*'):
        result = mul(a, b)
    if (operator == '/'):
        result = div(a, b)
    print("{} {} {} = {}".format(a, operator, b, result))
    sys.exit(0)
