#!/usr/bin/python3
from abc import ABC, abstractmethod
'''0. Abstract Animal Class and its Subclasses'''


class Animal(ABC):
    '''Abstract class Animal with an abstract method sound'''
    
    @abstractmethod
    def sound(self):
        '''Abstract method to be implemented by subclasses'''
        pass

class Dog(Animal):
    '''Dog class inheriting from Animal and implementing sound method'''
    
    def sound(self):
        return "Bark"

class Cat(Animal):
    '''Cat class inheriting from Animal and implementing sound method'''
    
    def sound(self):
        return "Meow"
