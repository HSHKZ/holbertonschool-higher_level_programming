#!/usr/bin/python3
'''13. Can I push'''


def add_attribute(obj, attr_name, attr_value):
    '''fonction qui ajoute un nouvel attribut'''
    if hasattr(obj, '__dict__'):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
