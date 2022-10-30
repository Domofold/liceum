#1
print('ZADANIE 1')
plik = open('szyfr1.txt','r')
wiersze = plik.readlines()
klucz1 = wiersze[6].split(' ')
def szyfrowanie(slowo,klucz):
    szyfr = list(slowo)
    for i in range(0, len(slowo)):
        indeks = int(klucz[i]) - 1
        szyfr[i], szyfr[indeks] = szyfr[indeks], szyfr[i]
    z = ''.join(szyfr)
    return z
for i in range(0,6):
    print(szyfrowanie(wiersze[i].strip(),klucz1))

#2
print('ZADANIE 2')
plik = open('szyfr2.txt','r')
wiersze = plik.readlines()
klucz2 = wiersze[1].split(' ')
def szyfrowanie2(slowo,klucz):
    szyfr = list(slowo)
    for i in range(0, len(slowo)):
        j = i % len(klucz)
        indeks = int(klucz[j]) - 1
        szyfr[i], szyfr[indeks] = szyfr[indeks], szyfr[i]
    z = ''.join(szyfr)
    return z
print(szyfrowanie2(wiersze[0].strip(),klucz2))

#3
plik_3 = open('szyfr3.txt', 'r')
wiersze = plik_3.readlines()

def odszyfruj_słowo(słowo, tablica):
    licznik = len(słowo) % len(tablica) - 1
    for i in range(len(słowo) - 1, -1, -1):
        if licznik == -1:
            licznik = len(tablica) - 1
        nowe_słowo = list(słowo)
        litera_do_zamiany = słowo[i]
        x = tablica[licznik]
        nowe_słowo[i] = słowo[tablica[licznik] - 1]
        nowe_słowo[tablica[licznik] - 1] = litera_do_zamiany
        słowo = ''.join(nowe_słowo)
        licznik -= 1
    return słowo

słowo = wiersze[0].strip()
klucz = [6, 2, 4, 1, 5, 3]
print('ZADANIE 3')
print(odszyfruj_słowo(słowo, klucz))







