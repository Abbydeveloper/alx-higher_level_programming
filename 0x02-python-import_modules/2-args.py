#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    length = len(sys.argv) - 1
    str = 0
    if (length == 0):
        str = "s."
    elif (length > 1):
        str = "s:"
    else:
        str = ":"

    print("{} argument{}".format(length, str))

    for n in range(1, length + 1):
        if (length > 0):
            print("{}: {}".format(n, sys.argv[n]))

