
'''

    Stiegelmayer Bálint
    Barizs Márton Dániel
    Kecskés Dominik Bálint

'''

szamok = []

for elem in range(1, 101):
    szamok.append(elem)


legnagyobb_szam = szamok[0]

for elem in szamok:
    if elem > legnagyobb_szam:
        legnagyobb_szam = elem

print("A listában talált legnagyobb szám a", legnagyobb_szam)
