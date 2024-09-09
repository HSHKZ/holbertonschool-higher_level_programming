#!/usr/bin/python3
def uniq_add(my_list=[]):
    resultat = 0
    for i in range(len(my_list)):
        for j in range(i):
            if my_list[i] == my_list[j]:
                my_list[i] = 0
        resultat += my_list[i]
    return resultat
