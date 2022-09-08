'''
    Stiegelmayer Bálint
    Barizs Márton Dániel
    Kecskés Dominik Bálint
'''

import random

szamok = []

for elem in range(1, 11):
    szamok.append(random.randint(1, 100))

print(szamok)

for elem_index in range(len(szamok)-1, 0, -1):
    max_index = elem_index
    for keresett in range(0, elem_index):
        if szamok[max_index] < szamok[keresett]:
            max_index = keresett
    csere = szamok[elem_index]
    szamok[elem_index] = szamok[max_index]
    szamok[max_index] = csere

print(szamok)
