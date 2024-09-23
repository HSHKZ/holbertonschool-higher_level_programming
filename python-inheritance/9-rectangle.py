#!/usr/bin/python3
'''9. Full rectangle'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''class Rectangle that inherits from BaseGeometry (7-base_geometry.py)'''

    def __init__(self, width, height):
        '''initialization of the class'''
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)

    def area(self):
        '''returns the area of the rectangle'''
        return self.__width * self.__height

    def __str__(self):
        '''return a string'''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
