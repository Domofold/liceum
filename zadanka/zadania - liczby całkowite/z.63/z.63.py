plik = open('ciagi.txt','r')
wiersze = plik.readlines()

#1
print('ZADANIE 1')
def czy_dwucykliczny(wiersz):
    if int(len(wiersz)) % 2 != 0:
        return False
    czesc1 = wiersz[0:int(len(wiersz)/2)]
    czesc2 = wiersz[int(len(wiersz)/2):len(wiersz)]
    if czesc1 == czesc2:
        return True
    return False
for wiersz in wiersze:
    wiersz = wiersz.strip()
    if czy_dwucykliczny(wiersz):
        print(wiersz.strip())

#2
print('ZADANIE 2')
ile = 0
def czy_jedynka_po_jedynce(wiersz):
    for i in range(0,len(wiersz)-1):
        if wiersz[i] == '1' and wiersz[i+1] == '1':
            return False
    return True

for wiersz in wiersze:
    wiersz = wiersz.strip()
    if czy_jedynka_po_jedynce(wiersz):
        ile += 1
print(ile)

#3
print('ZADANIE 3')

max_w_zbiorze = 0
for wiersz in wiersze:
    wiersz = wiersz.strip()
    if int(wiersz,2) > max_w_zbiorze:
        max_w_zbiorze = int(wiersz,2)

def czy_pierwsza(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for dzielnik in range(3,(n//2)+1,2):
        if n % dzielnik == 0:
            return False
    return True

zakres = []
for i in range(3,max_w_zbiorze//2,2):
    if i <= 1:
        continue
    if i == 2:
        zakres.append(i)
    if czy_pierwsza(int(i)):
        zakres.append(i)

def czy_polpierwsza(liczba):
    liczba = int(liczba,2)
    for i in range(0,len(zakres)):
        for j in range(i,len(zakres)):
            if liczba == zakres[i]*zakres[j]:
                return True
min = 2242342154125412
max = 0
ile = 0
for wiersz in wiersze:
    wiersz = wiersz.strip()
    if czy_polpierwsza(wiersz):
        ile += 1
        if int(wiersz,2) < min:
            min = int(wiersz,2)
        if int(wiersz,2) > max:
            max = int(wiersz,2)
print(f'ciagow: {ile}\nnajmniejsza: {min}\nnajwieksza{max}')




