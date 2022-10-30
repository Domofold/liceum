plik = open('slowa.txt', 'r')
wiersze = plik.readlines()

#1
print('ZADANIE 1')
ile = 0
for wiersz in wiersze:
    wiersz = wiersz.strip()
    ile_zer = 0
    for cyfra in wiersz:
        if cyfra == '0':
            ile_zer += 1
    ile_jedynek = len(wiersz) - ile_zer
    if ile_zer > ile_jedynek:
        ile += 1
print(ile)

#2
print('ZADANIE 2')
ile = 0
def czy_bloki(wiersz):
    pierwsza = wiersz[0]
    if pierwsza == '1':
        return False
    for i in range(0,len(wiersz)):
        ile_drugich = 0
        if wiersz[i] == pierwsza:
            continue
        else:
            druga = wiersz[i]
            for j in range(i, len(wiersz)):
                if wiersz[j] != druga:
                    return False
                else:
                    ile_drugich += 1
        if ile_drugich == 0:
            return False
        return True
T =[]
for wiersz in wiersze:
    if czy_bloki(wiersz.strip()):
        ile += 1
        T.append(wiersz.strip())
print(ile)

#3
print('ZADANIE 3')
slowa = []
najdluzszy_ciag = 0
for wiersz in wiersze:
    wiersz = wiersz.strip()
    wystapienia_max = 0
    wystapienia = 0
    for cyfra in wiersz:
       if cyfra == '0':
           wystapienia += 1
       else:
           wystapienia = 0
       if wystapienia > wystapienia_max:
           wystapienia_max = wystapienia
    if wystapienia_max > najdluzszy_ciag:
        najdluzszy_ciag = wystapienia_max
        slowa.clear()
    if wystapienia_max == najdluzszy_ciag:
        slowa.append(wiersz)
print(najdluzszy_ciag,slowa)

plik.close()


