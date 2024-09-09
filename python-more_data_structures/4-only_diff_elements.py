#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    nouvelle_liste = []
    for i in set_1:
        if i not in set_2:
            nouvelle_liste.append(i)
    for j in set_2:
        if j not in set_1:
            nouvelle_liste.append(j)
    return nouvelle_liste
