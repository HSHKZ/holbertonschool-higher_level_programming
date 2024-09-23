#!/usr/bin/python3
'''11. Square #2 '''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class Square that inherits from Rectangle (9-rectangle.py)'''

    def __init__(self, size):
        '''initialization of the class'''

        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        '''returns the area of the square'''
        return self.__size ** 2

    def __str__(self):
        '''return a string'''
        return "[Square] {}/{}".format(self.__size, self.__size)
