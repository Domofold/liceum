plik = open('instrukcje.txt','r')
wiersze = plik.readlines()

#1
dopisz = 0
usun = 0
for wiersz in wiersze:
    wiersz = wiersz.split()[0]
    if wiersz == 'DOPISZ':
        dopisz += 1
    elif wiersz == 'USUN':
        usun += 1
    continue
print(f'ZADANIE 1\n{dopisz - usun}')

#2
opcje = ['USUN','ZMIEN','DOPISZ','PRZESUN']
max_global = 0
zmienna = ''
for opcja in opcje:
    max = 0
    lokalny= 0
    for wiersz in wiersze:
        wiersz = wiersz.split()[0]
        if wiersz == opcja:
            lokalny += 1
        else:
            if lokalny > max:
                max = lokalny
            lokalny = 0
    if max > max_global:
        max_global = max
        zmienna = opcja
print(f'ZADANIE 2\n{zmienna} {max_global}')

#3
litera = ''
najwiecej = 0
slownik = {}
for wiersz in wiersze:
    litera = wiersz.split()[1].strip()
    wiersz = wiersz.split()[0]
    if wiersz == 'DOPISZ':
        if litera not in slownik.keys():
            slownik[litera] = 0
        slownik[litera] += 1
for klucz in slownik:
    if slownik[klucz] > najwiecej:
        najwiecej = slownik[klucz]
        litera = klucz
print(f'ZADANIE 3\n{litera} {najwiecej} razy')

#4
napis =''
for wiersz in wiersze:
    litera = wiersz.split()[1].strip()
    wiersz = wiersz.split()[0]
    if wiersz == 'DOPISZ':
        napis += litera
    elif wiersz == 'ZMIEN':
        napis = list(napis)
        napis.pop()
        napis.append(litera)
        napis = ''.join(napis)
    elif wiersz == 'USUN':
        napis = list(napis)
        napis.pop()
        napis = ''.join(napis)
    else:
        if litera != 'Z':
            indeks = napis.index(litera)
            napis = list(napis)
            napis[indeks] = chr(ord(litera) + 1)
            napis = ''.join(napis)
        else:
            indeks = napis.index(litera)
            napis = list(napis)
            napis[indeks] = 'A'
            napis = ''.join(napis)

print(f'ZADANIE 4\n{napis}')




