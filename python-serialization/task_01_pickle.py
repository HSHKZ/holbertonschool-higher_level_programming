#!/usr/bin/env python3
'''1. Pickling Custom Classes'''


import pickle


class CustomObject:
    '''custom Python class named CustomObject'''
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        # Your code here to serialize and save data to the specified file
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception as e:
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception as e:
            return None
