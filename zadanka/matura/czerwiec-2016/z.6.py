plik = open('liczby.txt','r')
wiersze = plik.readlines()

#1
print('ZADANIE 1')
ile_w_8 = 0
for i in range(0,len(wiersze)):
    if wiersze[i].strip()[len(wiersze[i].strip())-1] == '8':
        ile_w_8 += 1
print(ile_w_8)

#2
print('ZADANIE 2')
ile = 0
def czy_4(n):
    if wiersz[len(wiersz) - 1] == '4':
        return True
    return False

for wiersz in wiersze:
    wiersz = wiersz.strip()
    if czy_4(wiersz):
        for cyfra in wiersz:
            if cyfra == '0':
                break
        else:
            ile += 1


print(ile)

#3
print('ZADANIE 3')
ile_z_3 = 0
def czy_2(n):
    if wiersz[len(wiersz) - 1] == '2':
        return True
    return False
for wiersz in wiersze:
    wiersz = wiersz.strip()
    if czy_2(wiersz):
        if int(wiersz[0:len(wiersz)-1],2) % 2 == 0:
            ile_z_3 += 1
print(ile_z_3)

#4
print('ZADANIE 4')
suma = 0
def czy_8(n):
    if wiersz[len(wiersz) - 1] == '8':
        return True
    return False
for wiersz in wiersze:
    wiersz = wiersz.strip()
    if czy_8(wiersz):
        suma += int(wiersz[0:len(wiersz) - 1], int(wiersz[len(wiersz)-1]))
print(suma)

#5
print('ZADANIE 5')
max = 0
kod_max = ''
min = 10000000000000
kod_min = ''
for wiersz in wiersze:
    wiersz = wiersz.strip()
    liczba = int(wiersz[0:len(wiersz) - 1],int(wiersz[len(wiersz)-1]))
    if liczba > max:
        max = liczba
        kod_max = wiersz
    if liczba < min:
        min = liczba
        kod_min = wiersz
print(f'kod_max = {kod_max} liczba w systemie 10: {max}\nkod_min = {kod_min} liczba w systemie 10: {min}')