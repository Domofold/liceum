import math
plik_1 = open('dane_systemy1.txt', 'r')
plik_2 = open('dane_systemy2.txt', 'r')
plik_3 = open('dane_systemy3.txt', 'r')

wiersze_1 = plik_1. readlines()
wiersze_2 = plik_2. readlines()
wiersze_3 = plik_3. readlines()

min_1 = int(wiersze_1[0].split(' ')[1].strip(), 2)
min_2 = int(wiersze_2[0].split(' ')[1].strip(), 4)
min_3 = int(wiersze_3[0].split(' ')[1].strip(), 8)

for wiersz in wiersze_1:
    temperatura = int(wiersz.split(' ')[1].strip(), 2)
    if temperatura < min_1:
        min_1 = temperatura
for wiersz in wiersze_2:
    temperatura = int(wiersz.split(' ')[1].strip(), 4)
    if temperatura < min_2:
        min_2 = temperatura
for wiersz in wiersze_3:
    temperatura = int(wiersz.split(' ')[1].strip(), 8)
    if temperatura < min_3:
        min_3 = temperatura

min_1 = bin(min_1).replace('0b','')
min_2 = bin(min_2).replace('0b','')
min_3 = bin(min_3).replace('0b','')
zadania = open('wyniki_systemy_txt', 'a')
zadania.write('ZADANIE 1\n')
zadania.write(min_1)
zadania.write('\n')
zadania.write(min_2)
zadania.write('\n')
zadania.write(min_3)

s = 0
for i in range(1, 1095):
    if int(wiersze_1[i].split(' ')[0].strip(), 2) != 12 + i * 24 and int(wiersze_2[i].split(' ')[0].strip(), 4) != 12 + i * 24 and int(wiersze_3[i].split(' ')[0].strip(), 8) != 12 + i * 24:
        s += 1

zadania.write('\n\nZADANIE 2\n')
zadania.write(str(s))

suma = 1
max_1 = int(wiersze_1[0].split(' ')[1].strip(), 2)
max_2 = int(wiersze_2[0].split(' ')[1].strip(), 4)
max_3 = int(wiersze_3[0].split(' ')[1].strip(), 8)
for i in range(1,1095):
    s1 = int(wiersze_1[i].split(' ')[1].strip(), 2)
    s2 = int(wiersze_2[i].split(' ')[1].strip(), 4)
    s3 = int(wiersze_3[i].split(' ')[1].strip(), 8)
    if s1 > max_1 or s2 > max_2 or s3 > max_3:
        if s1 > max_1:
            max_1 = s1
        if s2 > max_2:
            max_2 = s2
        if s3 > max_3:
            max_3 = s3
        suma += 1

zadania.write('\n\nZADANIE 3\n')
zadania.write(str(suma))

max = int(wiersze_1[0].split(' ')[1].strip(), 2)
for i in range(0, 1095):
    for j in range(i + 1, 1095):
        if i != j:
            r = (int(wiersze_1[i].split(' ')[1].strip(), 2) - int(wiersze_1[j].split(' ')[1].strip(), 2))**2
            skok = math.ceil(r/(abs(i - j)))
            if skok > max:
                max = skok

zadania.write('\n\nZADANIE 4\n')
zadania.write(str(max))

plik_1.close()
plik_2.close()
plik_3.close()