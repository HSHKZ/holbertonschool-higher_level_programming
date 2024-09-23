#!/usr/bin/python3
'''1. My list'''


class MyList(list):
    """
    Represent a custom list named my list
    """

    def print_sorted(self):
        '''class MyList that inherits from list'''
        new_list = sorted(self)
        print(new_list)
        return new_list
