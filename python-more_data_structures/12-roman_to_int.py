#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    dict = {'I': 1, 'X': 10, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    valeur = 0
    i = 0
    for i in range(0, len(roman_string)-1):
        if dict[roman_string[i]] >= dict[roman_string[i+1]]:
            valeur += dict[roman_string[i]]
        else:
            valeur -= dict[roman_string[i]]
        i += 1
    if dict[roman_string[i]] > dict[roman_string[i-1]]:
        valeur += dict[roman_string[i]]
    else:
        valeur += dict[roman_string[i]]
    return valeur
