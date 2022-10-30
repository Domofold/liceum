import math
plik = open('dane_ulamki.txt', 'r')
wiersze = plik.readlines()

#1

T = []
min = 10000
for wiersz in wiersze:
    wiersz = wiersz.strip().split(' ')
    wynik = int(wiersz[0]) / int(wiersz[1])
    if wynik <= min:
        if wynik != min:
            T.clear()
        T.append(wiersz)
        min = wynik

odp =open('wyniki_ulamki.txt','w')
odp.write(f'ZADANIE 1\nnajmniejszy ulamek: {T[0][0]} {T[0][1]}')

#2

import math
ile_w_nieskracalnej = 0
for wiersz in wiersze:
    licznik = int(wiersz.strip().split(' ')[0])
    mianownik = int(wiersz.strip().split(' ')[1])
    if math.gcd(licznik,mianownik) == 1:
        ile_w_nieskracalnej += 1
odp.write(f'\nZADANIE 2\nulamkow w postaci nieskrcalnej: {ile_w_nieskracalnej}')

#3

suma = 0
for wiersz in wiersze:
    licznik = int(wiersz.strip().split(' ')[0])
    mianownik = int(wiersz.strip().split(' ')[1])
    licznik = int(licznik / math.gcd(licznik, mianownik))
    suma += licznik
odp.write(f'\nZADANIE 3\nsuma licznikow: {suma}')

#4

szukane = 0
b= 2**2 * 3**2 * 5**2 * 7**2 * 13
for wiersz in wiersze:
    licznik = int(wiersz.strip().split(' ')[0])
    mianownik = int(wiersz.strip().split(' ')[1])
    szukane += int(licznik * b / mianownik)

odp.write(f'\nZADANIE 4 poszukiwana wartosc: {szukane}')
