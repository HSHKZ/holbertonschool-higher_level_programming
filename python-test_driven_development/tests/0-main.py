#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer
print(add_integer(1, 2))              # 3
print(add_integer(100, -2))           # 98
print(add_integer(2))                 # 100
print(add_integer(100.3, -2))         # 98
try:
    print(add_integer(4, "School"))   # TypeError: b must be an integer
except Exception as e:
    print(e)
try:
    print(add_integer(None))          # TypeError: a must be an integer
except Exception as e:
    print(e)
