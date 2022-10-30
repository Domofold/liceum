import math
plik = open('liczby.txt', 'r')
wiersze = plik.readlines()
odp = open('wyniki.txt', 'w')
T = []
for wiersz in wiersze:
    x = int(wiersz.strip())
    if x < 1000:
        T.append(x)
ilosc_liczb = len(T)
przedostatnia = T[len(T) - 2]
ostatnia = T[len(T) - 1]

odp.write('ZADANIE 1\n')
odp.write(f'liczb mniejszych od 1000: {ilosc_liczb}\n')
odp.write(f'dwie ostatnie liczby: {przedostatnia}, {ostatnia}')

odp.write('\n\nZADANIE 2\n')
for wiersz in wiersze:
    T = []
    liczba = int(wiersz.strip())
    for dzielnik in range(1, liczba // 2 + 1):
        if liczba % dzielnik == 0:
            T.append(dzielnik)
    T.append(liczba)
    if len(T) == 18:
        odp.write(f'liczba: {liczba}, dzielniki: {T}\n')

odp.write('\n\nZADANIE 3\n')

max = -math.inf
for i in range(0, len(wiersze)):
    czy_względnie_pierwsza = True
    for j in range(0, len(wiersze)):
        if i == j:
            continue
        liczba_1 = int(wiersze[i])
        liczba_2 = int(wiersze[j])
        if math.gcd(liczba_1, liczba_2) > 1:
            czy_względnie_pierwsza = False

    if czy_względnie_pierwsza:
        if int(wiersze[i]) > max:
            max = int(wiersze[i])
odp.write(f'najwieksza wzglednie pierwsza: {max}')



