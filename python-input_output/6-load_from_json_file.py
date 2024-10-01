#!/usr/bin/python3
'''6. Create object from a JSON file'''


def load_from_json_file(filename):
    '''function that creates an Object from a "JSON file"'''
    import json
    with open(filename) as f:
        return json.load(f)
