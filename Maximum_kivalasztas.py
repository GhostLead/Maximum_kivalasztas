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
    max_index = 0
    csere1 = szamok[elem_index]
    csere2 = 0
    for keresett in range(0, elem_index):
        if szamok[max_index] < szamok[keresett]:
            max_index = keresett
            csere2 = szamok[max_index]
    if csere2 > 0:
        szamok.pop(max_index)
        szamok.insert(max_index, csere1)
        szamok.pop(elem_index)
        szamok.insert(elem_index, csere2)
        print(szamok)

print(szamok)
