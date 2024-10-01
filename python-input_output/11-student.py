#!/usr/bin/python3
'''11. Student to disk and reload'''


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            dictionnaire_filtre = {}
            for attr in attrs:
                if isinstance(attr, str) and hasattr(self, attr):
                    dictionnaire_filtre[attr] = getattr(self, attr)
            return dictionnaire_filtre
        else:
            return vars(self)

    def reload_from_json(self, json):
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
