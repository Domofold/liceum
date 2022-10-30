plik = open('pary.txt','r')
wiersze = plik.readlines()

#1
print('ZADANIE 1')
def czy_pierwsza(wiersz):
    if wiersz <=1:
        return False
    if wiersz % 2 == 0:
        return True
    for dzielnik in range(3,int((wiersz/2)+1),2):
        if wiersz % dzielnik == 0:
            return False
    return True
def pierwsze_zakres(slowo):
    pierwsze = []
    if slowo > 2:
        pierwsze.append(2)
    for i in range(3,slowo,2):
        if czy_pierwsza(i):
            pierwsze.append(i)
    return pierwsze

for wiersz in wiersze:
    wiersz = int(wiersz.split()[0].strip())
    if wiersz in (1, 2, 3, 4) or wiersz % 2 != 0:
        continue
    pary = []
    if wiersz % 2 == 0 and wiersz > 4:
        pierwsze = pierwsze_zakres(wiersz)
        for i in pierwsze:
            for j in range(pierwsze.index(i),len(pierwsze)):
                if i + pierwsze[j] == wiersz:
                    pary.append(i)
                    pary.append(pierwsze[j])
    if len(pary) == 2:
        print(f'{wiersz} {pary[0]} {pary[1]}')
    else:
        wlasciwe = [pary[0],pary[1]]
        for i in range(2,len(pary)-1,2):
                if abs(pary[i] - pary[i+1]) > abs(wlasciwe[0] - wlasciwe[1]):
                    wlasciwe.clear()
                    wlasciwe.append(pary[i])
                    wlasciwe.append(pary[i+1])
        print(f'{wiersz} {wlasciwe[0]} {wlasciwe[1]}')

#2
print('ZADANIE 2')

def najdluzszy_fragment(slowo):
    obecna_litera = slowo[0]
    dlugosc = 1
    wystapienia = 1
    wynik = (obecna_litera * dlugosc, dlugosc)
    for i in range(1, len(slowo)):
        if obecna_litera == slowo[i]:
            wystapienia += 1
        else:
            obecna_litera = slowo[i]
            wystapienia = 1
        if wystapienia > dlugosc:
            dlugosc = wystapienia
            wynik = (obecna_litera * dlugosc, dlugosc)
    return wynik

for wiersz in wiersze:
    wiersz = wiersz.split(' ')[1].strip()
    print(f'{najdluzszy_fragment(wiersz)[0]} {len(najdluzszy_fragment(wiersz)[0])}')

#3
print('ZADANIE 3')

def mniejsza(liczba1, slowo1, liczba2, slowo2):
    if liczba1 < liczba2:
        return [liczba1, slowo1]
    if liczba1 > liczba2:
        return [liczba2, slowo2]
    else:
        for i in range(0, len(slowo1)):
            if slowo1[i] == slowo2[i]:
                continue
            if ord(slowo1[i]) < ord(slowo2[i]):
                return [liczba1, slowo1]
            if ord(slowo1[i]) > ord(slowo2[i]):
                return [liczba2, slowo2]

T = []
for wiersz in wiersze:
    wiersz = wiersz.split(' ')
    if int(wiersz[0].strip()) == len(wiersz[1].strip()):
        T.append([int(wiersz[0].strip()), wiersz[1].strip()])

min = [T[0][0], T[0][1]]
for i in range(0,len(T)):
    for j in range(i+1,len(T)):
        lokal = mniejsza(T[i][0],T[i][1],T[j][0],T[j][1])
        if mniejsza(min[0],min[1],lokal[0],lokal[1]) == lokal:
            min = lokal
print(min)



