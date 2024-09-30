#!/usr/bin/python3
"""adding some doc here to see if checker want it"""

def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
