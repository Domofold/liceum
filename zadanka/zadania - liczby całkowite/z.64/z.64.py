plik = open('dane_obrazki.txt', 'r')
wiersze = plik.readlines()

#1
max_czarnych = 0
ile_rewersow = 0

for i in range(0,len(wiersze),22):
    ile_bialych = 0
    ile_czarnych = 0
    for j in range(0,20):
        wiersz = wiersze[i + j][:20]
        for piksel in wiersz:
            if piksel == '1':
                ile_czarnych += 1
            else:
                ile_bialych += 1
    if ile_czarnych > ile_bialych:
        ile_rewersow += 1
    if ile_czarnych > max_czarnych:
        max_czarnych = ile_czarnych
odp = open('wyniki_obrazki.txt','w')
odp.write(f'ZADANIE 1\nLICZBA REWERSOW: {ile_rewersow}\nNAJWIECEJ CZARNYCH PIKSELI: {max_czarnych}')

#2
opis = []
ile_rekurencyjnych = 0
for i in range(0, len(wiersze), 22):
    T1 = ''
    T2 = ''
    T3 = ''
    T4 = ''
    for j in range(0,10):
        for piksel in range(0, 10):
            T1 += wiersze[i + j].strip()[piksel]
        for piksel in range(10,20):
            T2 += wiersze[i + j].strip()[piksel]
    for j in range(10,20):
        for piksel in range(0, 10):
            T3 += wiersze[i + j].strip()[piksel]
        for piksel in range(10,20):
            T4 += wiersze[i + j].strip()[piksel]
    if T1 == T2 == T3 == T4:
        ile_rekurencyjnych += 1
        if ile_rekurencyjnych == 1:
            for j in range(0,20):
                opis.append(wiersze[i + j][:20])



odp.write(f'\nZADANIE 2\nLICZBA REKURENCYJNYCH OBRAZKOW: {ile_rekurencyjnych}\nPIERWSZY WYSTEPUJACY OBRAZEK REKURENCYJNY:\n')
for i in opis:
    odp.write(f'{i}\n')

#3

poprawne = 0
naprawialne = 0
nienaprawialne = 0
max_bledow = 0

for i in range(0,len(wiersze), 22):
    blednych_kolumn = 0
    blednych_wierszy = 0
    for j in range(0,20):
        suma_1 = 0
        for l in range(0,21):
            suma_1 += int(wiersze[i+j][l])
        if suma_1 % 2 != 0:
            blednych_kolumn += 1
        suma_2 = 0
        for l in range(0,21):
            suma_2 += int(wiersze[l + i][j])
        if suma_2 % 2 != 0:
            blednych_wierszy += 1
    if blednych_wierszy + blednych_kolumn > max_bledow:
        max_bledow = blednych_wierszy + blednych_kolumn
    if blednych_wierszy == 0 and blednych_kolumn == 0:
        poprawne += 1
    elif blednych_wierszy <= 1 and blednych_kolumn <= 1:
        naprawialne += 1
    else:
        nienaprawialne += 1
odp.write(f'ZADANIE 3\nPOPRAWNYCH: {poprawne}\nNAPRAWIALNYCH: {naprawialne}\nNIENAPRAWIALNE: {nienaprawialne}\nNAJWIECEJ BLEDOW: {max_bledow}')

#4
odp.write(f'\nZADANIE4\n')
for i in range(0,len(wiersze), 22):
    blednych_kolumn = 0
    blednych_wierszy = 0
    wiersz = 0
    kolumna = 0
    for j in range(0,20):
        suma_1 = 0
        for l in range(0,21):
            suma_1 += int(wiersze[i+j][l])
        if suma_1 % 2 != 0:
            blednych_kolumn += 1
            kolumna = j
        suma_2 = 0
        for l in range(0,21):
            suma_2 += int(wiersze[l + i][j])
        if suma_2 % 2 != 0:
            blednych_wierszy += 1
            wiersz = j
    if blednych_wierszy == 0 and blednych_kolumn == 0:
        continue
    elif blednych_wierszy <= 1 and blednych_kolumn <= 1:
        if blednych_wierszy == 1 and blednych_kolumn == 0:
            odp.write(f'numer obrazka: {i//22 + 1} wiersz: {wiersz}\n')
        elif blednych_kolumn == 1 and blednych_wierszy == 0:
            odp.write(f'numer obrazka: {i // 22 + 1} kolumna: {kolumna}\n')
        else:
            odp.write(f'numer obrazka: {i // 22 + 1} wiersz: {wiersz} kolumna: {kolumna}\n')

