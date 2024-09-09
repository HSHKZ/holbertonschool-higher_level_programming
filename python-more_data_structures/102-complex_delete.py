#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    cle_a_supprimer = \
        [key for key in a_dictionary if a_dictionary[key] == value]
    for key in cle_a_supprimer:
        del a_dictionary[key]
    return a_dictionary
