#!/usr/bin/env python3
'''4. The Enigmatic FlyingFish - Exploring Multiple Inheritance'''


class Fish:
    '''class Fish'''
    def __init__(self):
        '''initialization of the class'''
        Fish.__init__(self)

    def swim(self):
        '''méthode swim'''
        print("The flying fish is swimming")

    def habitat(self):
        '''méthode habitat'''
        print("The fish lives in water")

class Bird:
    '''class Bird'''
    def __init__(self):
        '''initialization of the class'''
        Bird.__init__(self)

    def fly(self):
        '''méthode fly'''
        print("The bird is flying")

    def habitat(self):
        '''méthode habitat'''
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    '''class FlyingFish qui hérite de Fish et Bird'''
    def __init__(self):
        '''initialization of the class'''
        pass

    def swim(self):
        '''méthode swim'''
        print("The flying fish is swimming!")

    def fly(self):
        '''méthode fly'''
        print("The flying fish is soaring!")

    def habitat(self):
        '''méthode habitat'''
        print("The flying fish lives both in water and the sky!")
