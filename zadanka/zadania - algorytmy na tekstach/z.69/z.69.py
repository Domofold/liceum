plik = open('dane_geny.txt', 'r')
wiersze = plik.readlines()

#z.1
T = []
for i in range(0, 501):
    T.append(0)

for i in range(0, len(wiersze)):
    T[len(wiersze[i].strip())] += 1
ile_gatunkow = 0
najwiecej = 0
for i in range(0,501):
    if T[i] != 0:
        ile_gatunkow += 1
    if T[i] > najwiecej:
        najwiecej = T[i]

odp = open('odp.txt', 'w')
odp.write(f'ZADANIE 1\nliczba gatunkow: {ile_gatunkow}\nnajwiecej osobnikow gatunku: {najwiecej}')

#z.2
def znajdz_geny(n):
    geny = []
    index = 0
    for i in range(0, len(n) - 1):
        if index > i:
            continue
        if n[i] == 'A' and n[i + 1] == 'A':
            gen = 'AA'
            for j in range (i + 2, len(n) - 1):
                if n[j] == 'B' and n[j + 1] =='B':
                    gen += 'BB'
                    index = j + 2
                    geny.append(gen)
                    break
                gen += n[j]
    return geny
mutacje = 0
for wiersz in wiersze:
    wiersz = wiersz.strip()
    geny = znajdz_geny(wiersz)
    for i in geny:
        if i.find('BCDDC') != -1:
            mutacje += 1
odp.write(f'\nZADANIE 2\nwystapien mutacji: {mutacje}')

#z.3
najwieksza_liczba = 0
dlugosc = 0
for wiersz in wiersze:
    wiersz = wiersz.strip()
    geny = znajdz_geny(wiersz)
    if len(geny) > najwieksza_liczba:
        najwieksza_liczba = len(geny)
    for gen in geny:
        if len(gen) > dlugosc:
            dlugosc = len(gen)
odp.write(f'\nZADANIE 3\nnajwieksza liczba genow: {najwieksza_liczba}\nnajdluzszy gen: {dlugosc}')

#z.4
#mozna uzyc [::-1]
def czy_palindrom(genotyp):
    i = 0
    j = len(genotyp) - 1
    while i < j:
        if genotyp[i] == genotyp[j]:
            i += 1
            j -= 1
        else:
            return False
    return True
ile_silnie_odpornych = 0

for wiersz in wiersze:
    wiersz = wiersz.strip()
    if czy_palindrom(wiersz):
        ile_silnie_odpornych += 1
print(ile_silnie_odpornych)

ile_odpornych = 0
for wiersz in wiersze:
    wiersz = wiersz.strip()
    geny = znajdz_geny(wiersz)
    odwrocone = wiersz[::-1]
    geny_odwrocone = znajdz_geny(odwrocone)
    if geny == geny_odwrocone:
        ile_odpornych += 1
print(ile_odpornych)














