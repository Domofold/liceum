import math
plik = open('ciagi.txt', 'r')
plik_bledne = open('bledne.txt', 'r')

wiersze = plik.readlines()
wiersze_bledne = plik_bledne.readlines()

ile_art = 0
r = 0
max = 0
for i in range(1, len(wiersze), 2):
    liczby = wiersze[i].strip().split(' ')
    czy = True
    r = int(liczby[1]) - int(liczby[0])
    for j in range(0, len(liczby) - 1):
        if r != int(liczby[j + 1]) - int(liczby[j]):
            czy = False
            break
    if czy:
        ile_art += 1
    if r > max:
        max = r
odp = open('wyyniki.txt', 'w')
odp.write(f'ZADANIE 1\nciagow arytmetycznych: {ile_art}\nnajwieksza roznica: {max}')
odp.write('\n\nZADANIE 2')
s = 0
for i in range(1, len(wiersze), 2):
    max = -math.inf
    liczby = wiersze[i].strip().split(' ')
    for liczba in liczby:
        if round(pow(int(liczba), 1/3),5).is_integer():
            if int(liczba) > max:
                max = int(liczba)
    if max > -math.inf:
        s+=1
        odp.write(f'\n{max}')

odp.write('\n\nZADANIE 3')
for i in range(1, len(wiersze_bledne), 2):
    roznice = []
    liczby = wiersze_bledne[i].strip().split(' ')
    for j in range(0, len(liczby) - 1):
        roznice.append(int(liczby[j + 1]) - int(liczby[j]))
    if roznice[0] != roznice[1] and roznice[1] == roznice[2]:
        odp.write(liczby[0])
        continue
    if roznice[0] != roznice[2] and roznice[1] != roznice[2] and roznice[2] == roznice[3]:
        odp.write(liczby[1])
        continue
    for j in range(0, len(liczby)):
        if roznice[j] != roznice[0]:
            odp.write(f'\n{liczby[j + 1]}')
            break


