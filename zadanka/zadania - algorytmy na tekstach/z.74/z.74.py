plik = open('hasla.txt', 'r')
wiersze = plik.readlines()

#1
cyfry =['0','1','2','3','4','5','6','7','8','9']
def czy_numeryczny(haslo):
    for i in range(0,len(haslo)):
        if haslo[i] not in cyfry:
            return False
    return True

ile_numerycznych = 0
for wiersz in wiersze:
    wiersz = wiersz.strip()
    if czy_numeryczny(wiersz):
        ile_numerycznych += 1
odp = open('wyniki_hasla.txt', 'w')
odp.write(f'ZADANIE 1\n {ile_numerycznych}')

#2
hasla = []
slownik = {}
for wiersz in wiersze:
    wiersz = wiersz.strip()
    if wiersz in slownik.keys():
        slownik[wiersz] += 1
        continue
    slownik[wiersz] = 1
for haslo in slownik.keys():
    if slownik[haslo] >= 2:
        hasla.append(haslo)
odp.write('\nZADANIE 2\n')
hasla.sort()
for i in hasla:
    odp.write(f'{i}\n')

#3

ile = 0
def czy_wystepuje(haslo):
    for i in range(0,len(haslo) - 3):
        posortowana = sorted([ord(haslo[i]), ord(haslo[i + 1]), ord(haslo[i + 2]), ord(haslo[i + 3])])
        suma4 = ord(haslo[i]) + ord(haslo[i + 1]) + ord(haslo[i + 2]) + ord(haslo[i + 3])
        sumaascii = posortowana[0] * 4 + 6
        if posortowana[3] - posortowana[0] <= 3:
            return True
    return False

for wiersz in wiersze:
    wiersz = wiersz.strip()
    if czy_wystepuje(wiersz):
        ile += 1

odp.write(f'ZADANIE 3\n{ile}')
#4

def czy_spelnia_warunki(haslo):
    spelnionych = 0
    numeryczne = ['0','1','2','3','4','5','6','7','8','9']
    male_litery = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    for znak in haslo:
        if znak in numeryczne:
            spelnionych += 1
            break
    for znak in haslo:
        if znak in male_litery:
            spelnionych += 1
            break
    for znak in haslo:
        if 65 <= ord(znak) <= 90:
            spelnionych += 1
            break
    if spelnionych == 3:
        return True
    return False

liczba = 0
for wiersz in wiersze:
    wiersz = wiersz.strip()
    if czy_spelnia_warunki(wiersz):
        liczba += 1
odp.write(f'\nZADANIE4\n{liczba}')
