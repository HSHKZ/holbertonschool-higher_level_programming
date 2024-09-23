#!/usr/bin/env python3
'''5. The Mystical Dragon - Mastering Mixins'''

class SwimMixin:
    '''class SwimMixin'''
    def swim(self):
        '''méthode swim'''
        print("The creature swims!")

class FlyMixin:
    '''class FlyMixin'''
    def fly(self):
        '''méthode fly'''
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    '''class Dragon'''
    def roar(self):
        '''initialization of the class'''
        print("The dragon roars!")
