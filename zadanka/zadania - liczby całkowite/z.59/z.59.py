import math
plik = open('liczby.txt', 'r')
liczby = plik.readlines()

s = 0
for liczba in liczby:
    liczba = int(liczba)
    if liczba % 2 == 0:
        continue
    T = set()
    dz = 3
    while liczba > 1 and dz <= math.sqrt(liczba):
        while liczba % dz == 0:
            T.add(dz)
            liczba = liczba / dz
        dz += 2
    if liczba > 1:
        T.add(liczba)
    if len(T) == 3:
        s += 1
wyniki = open('wyniki_liczby.txt', 'w')
wyniki.write('ZADANIE 1\n')
wyniki.write(str(s))


ile_liczb = 0
for liczba in liczby:
    liczba = liczba.strip()
    odwrocona = liczba[::-1]
    suma = int(liczba) + int(odwrocona)
    if int(suma) == int(str(suma)[::-1]):
        ile_liczb += 1

wyniki.write('\n\nZADANIE 2\n')
wyniki.write(str(ile_liczb))

max = -math.inf
min = math.inf
wynik = 0
taabela = [0,0,0,0,0,0,0,0]
for liczba in liczby:
    z = int(liczba)
    iloczyn = 1
    moc = 0
    while len(liczba.strip()) > 1:
        moc += 1
        for cyfra in liczba.strip():
            iloczyn *= int(cyfra)
        liczba = str(iloczyn)
    if moc == 1:
        if z > max:
            max = z
        if z < min:
            min = z
    if 1 <= moc <= 8:
        taabela[moc - 1] = int(taabela[moc - 1]) + 1

for k in taabela:
    print(k)
print(max)
print(min)










