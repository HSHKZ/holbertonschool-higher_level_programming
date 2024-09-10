#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
    except stderr:
        print("Exception: {:d}".format(stderr))
