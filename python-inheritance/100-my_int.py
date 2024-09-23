#!/usr/bin/python3
'''12. My integer'''


class MyInt(int):
    '''class Square that inherits from Rectangle (9-rectangle.py)'''

    def __eq__(self, other):
        # Invert the equality operator
        return super().__ne__(other)

    def __ne__(self, other):
        # Invert the inequality operator
        return super().__eq__(other)
