#!/usr/bin/python3
'''3. To JSON string'''


def to_json_string(my_obj):
    '''function that returns the JSON representation of an object (string)'''
    import json
    return json.dumps(my_obj)
