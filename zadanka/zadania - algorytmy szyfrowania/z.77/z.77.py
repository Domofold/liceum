plik = open('dokad.txt','r')
wiersz = plik.readlines()
wiersz = ''.join(wiersz)
import math
#1
def szyfr_vigenera(slowo, klucz):
    szyfr = ''
    nr = -1
    for i in slowo:
        if i == '.' or i == ' ' or i == ',':
            szyfr += i
            continue
        nr += 1
        index_klucza = nr % len(klucz)
        przesuniecie = ord(klucz[index_klucza]) - 65
        if ord(i) + przesuniecie <= 90:
            szyfr += chr(ord(i) + przesuniecie)
        else:
            szyfr += chr(przesuniecie + ord(i) - 26)
    ile_kluczy = math.ceil(nr / len(klucz))
    return szyfr, ile_kluczy
print(szyfr_vigenera(wiersz,'LUBIMYCZYTAC'))

#2
print('ZADANIE 2')
plik2 = open('szyfr.txt','r')
wiersze = plik2.readlines()
szyfr = wiersze[0].strip()
klucz = wiersze[1].strip()
def deszyfrowanie_vigenera(szyfr,klucz):
    slowo = ''
    nr = -1
    for i in szyfr:
        if i in (' ',',','.'):
            slowo += i
            continue
        nr += 1
        index_klucza = nr % len(klucz)
        przesuniecie = ord(klucz[index_klucza]) - 65
        if ord(i) - przesuniecie < 65:
            slowo += chr(ord(i) - przesuniecie + 26)
        else:
            slowo += chr(ord(i) - przesuniecie)
    return slowo
print(deszyfrowanie_vigenera(szyfr,klucz))

#3
print('ZADANIE 3')
T = {}
for i in range(0,26):
    T[str(chr(65 + i))] = 0
for i in szyfr:
    if i not in(' ',',','.'):
        T[i] += 1
print(T)
n = 0
for wartosc in T.values():
    n += wartosc
ko_licznik = 0
for wartosc in T.values():
    ko_licznik += wartosc * (wartosc - 1)
ko = ko_licznik / (n*(n - 1))
d = 0.0285 / (ko - 0.0385)
d = round(d,2)
print(f'przybliżenie {d}')
print(len(klucz))

