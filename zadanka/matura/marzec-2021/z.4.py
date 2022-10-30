plik = open('galerie.txt','r')
wiersze = plik.readlines()

#1
slownik = {}
for wiersz in wiersze:
    wiersz = wiersz.split(' ')
    if wiersz[0] in slownik.keys():
        continue
    else:
        slownik[wiersz[0]] = 0
for wiersz in wiersze:
    wiersz = wiersz.split(' ')
    slownik[wiersz[0]] += 1
print('ZADANIE 1')
for i in slownik.keys():
    print(f'{i} {slownik[i]}')

#2
print('ZADANIE 2\na)')
#a
slownik = {}
for wiersz in wiersze:
    wiersz = wiersz.split(' ')
    powierzchnia = 0
    ile_lokali = 0
    for i in range(2,len(wiersz),2):
        powierzchnia += int(wiersz[i]) * int(wiersz[i+1])
        if str(wiersz[i]) != '0':
            ile_lokali += 1
    slownik[wiersz[1]] = powierzchnia
    print(f'{wiersz[1]} {powierzchnia} {ile_lokali}')

#b
miasto_max = ''
miasto_min = ''
min = 100000000002930930293
max = 0
print('b)')
for i in slownik.keys():
    if slownik[i] > max:
        max = slownik[i]
        miasto_max = i
    if slownik[i] < min:
        min = slownik[i]
        miasto_min = i
print(f'{miasto_max} {max}\n{miasto_min} {min}')

#3
print('ZADANIE 3')
miasto_lmax = ''
lmax = 0
miasto_lmin = ''
lmin = 343049432429382342341234
for wiersz in wiersze:
    wiersz = wiersz.split(' ')
    powierzchnie = set()
    ile_rownych = 0
    for i in range(2,len(wiersz),2):
        if int(wiersz[i]) != 0:
            powierzchnie.add(int(wiersz[i])*int(wiersz[i+1]))
    if len(powierzchnie) > lmax:
        lmax = len(powierzchnie)
        miasto_lmax = wiersz[1]
    if len(powierzchnie) < lmin:
        lmin = len(powierzchnie)
        miasto_lmin = wiersz[1]
print(f'{miasto_lmax} {lmax}\n{miasto_lmin} {lmin}')

