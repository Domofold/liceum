import math
plik_1 = open('liczby1.txt','r')
wiersze_1 = plik_1.readlines()
plik_2 = open('liczby2.txt', 'r')
wiersze_2 = plik_2.readlines()

#1
max = -math.inf
min = math.inf

for wiersz in wiersze_1:
    wiersz = wiersz.strip()
    if int(wiersz) > max:
        max = int(wiersz)
    if int(wiersz) < min:
        min = int(wiersz)
odp = open('wyniki.txt', 'w')
odp.write(f'ZADANIE 1\nmax = {max}\nmin = {min}')

#2
T =[]
dlugosc = 0
i = -1
for wiersz in wiersze_2:
    wiersz = wiersz.strip()
    A = []
    i += 1
    for j in range(i, len(wiersze_2) - 1):
        if int(wiersze_2[i + 1].strip()) >= int(wiersze_2[j].strip()):
            A.append(wiersze_2[j].strip())
            i += 1
        else:
            A.append(wiersze_2[i].strip())
            if len(A) > dlugosc:
                T.clear()
                T.append(A[0])
                dlugosc = len(A)
                A.clear()
            break
odp.write(f'\nZADANIE 2\nliczba elementow : {dlugosc}\npierwszy element: {T[0]}')

#3

ile_rownych = 0
plik_1_wiekszy_od_plik_2 = 0
for i in range(0, len(wiersze_1)):
    wiersz_1 = wiersze_1[i].strip()
    wiersz_2 = wiersze_2[i].strip()
    if int(wiersz_1, 8) == int(wiersz_2):
        ile_rownych += 1
    elif int(wiersz_1, 8) > int(wiersz_2):
        plik_1_wiekszy_od_plik_2 += 1

odp.write(f'\nZADANIE 3\nrownych: {ile_rownych}\nliczba1 > liczba2: {plik_1_wiekszy_od_plik_2} ')

#4

ile_w_10 = 0
ile_w_8 = 0
for wiersz in wiersze_2:
    liczba = wiersz.strip()
    liczba_8 = str(oct(int(liczba))[2:])
    for cyfra in range(0,len(liczba)):
        if int(liczba[cyfra]) == 6:
            ile_w_10 += 1
    for cyfra in range(0, len(liczba_8)):
        if int(liczba_8[cyfra]) == 6:
            ile_w_8 += 1

odp.write(f'\nZADANIE 4\nszostek w dziesietnym: {ile_w_10}\nszostek w osemkowym: {ile_w_8}')

