#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as stderr:
        import sys
        print("Exception: {}".format(stderr), file=sys.stderr)
        return None
