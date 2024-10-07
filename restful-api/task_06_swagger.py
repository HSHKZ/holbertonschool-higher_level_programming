#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import *
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]
    if operator == '+':
        resultat = add(a, b)
        print("{} + {} = {}" .format(a, b, resultat))
    elif operator == '-':
        resultat = sub(a, b)
        print("{} - {} = {}" .format(a, b, resultat))
    elif operator == '*':
        resultat = mul(a, b)
        print("{} * {} = {}" .format(a, b, resultat))
    elif operator == '/':
        resultat = div(a, b)
        print("{} / {} = {}" .format(a, b, resultat))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
