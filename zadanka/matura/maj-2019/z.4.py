import math
plik = open('liczby.txt','r')
wiersze = plik.readlines()

#1
print('ZADANIE 1')
def czy_potega_3(liczba):
    while liczba != 1:
        if liczba % 3 == 0:
            liczba = liczba / 3
        else:
            return False
    return True

ile = 0
for wiersz in wiersze:
    wiersz = int(wiersz.strip())
    if czy_potega_3(wiersz):
        ile += 1
print(f'ilość liczb, które są potęgą trójki: {ile}')

#2
print('ZADANIE 2')
def czy_silnie_rowne_liczbie(liczba):
    liczba = str(liczba)
    suma = 0
    for cyfra in liczba:
        suma += math.factorial(int(cyfra))
    if suma == int(liczba):
        return True
    return False

print(f'liczby, które są równe sumie silni swoich cyfr:')
A = []
for wiersz in wiersze:
    wiersz = int(wiersz.strip())
    if czy_silnie_rowne_liczbie(wiersz):
        A.append(wiersz)
        print(wiersz)

#3
print('ZADANIE 3')
max_pierwsza_liczba = 0
max_dlugosc = 0
max_nwd = 0

for i in range(0, len(wiersze)):
    obecna_dlugosc = 1
    pierwsza_liczba = int(wiersze[i])
    pierwsze_nwd = pierwsza_liczba
    for j in range(i+1, len(wiersze)):
        obecna_liczba = int(wiersze[j])
        obecne_nwd = math.gcd(pierwsze_nwd, obecna_liczba)
        if obecne_nwd > 1:
            pierwsze_nwd = obecne_nwd
            obecna_dlugosc += 1
        if obecne_nwd == 1:
            break
    if obecna_dlugosc > max_dlugosc:
        max_dlugosc = obecna_dlugosc
        max_pierwsza_liczba = pierwsza_liczba
        max_nwd = pierwsze_nwd

print('\nZADANIE 4.3.')
print(f'''DŁUGOSC: {max_dlugosc}''')
print(f'''PIERWSZA LICZBA: {max_pierwsza_liczba}''')
print(f'''DZIELNIK: {max_nwd}''')




