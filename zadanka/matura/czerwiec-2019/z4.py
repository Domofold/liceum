plik = open('liczby.txt','r')
liczby = plik.readlines()
plik2 = open('pierwsze.txt','r')
pierwsze = plik2.readlines()

#1
print('ZADANIE 1')

def czy_pierwsza(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for dzielnik in range(3,int((n/2)+1),2):
        if n % dzielnik == 0:
            return False
    return True

T = []
for wiersz in liczby:
    liczba = int(wiersz.strip())
    if czy_pierwsza(liczba):
        if liczba >= 100 and liczba <= 5000:
            T.append(liczba)
print(T)

#2
print('ZADANIE 2')
A = []
for wiersz in pierwsze:
    liczba = int(wiersz.strip())
    odwrocona = int(str(liczba)[::-1])
    if czy_pierwsza(odwrocona):
        A.append(liczba)
print(A)

#3
print('ZADANIE 3')
ile = 0
for wiersz in pierwsze:
    liczba = wiersz.strip()
    x = True
    s = 0
    while x:
        for i in liczba:
            i = int(i)
            s += i
        liczba = str(s)
        if int(liczba) < 10:
            x = False
        if s == 1:
            ile += 1
        s = 0
print(ile)

