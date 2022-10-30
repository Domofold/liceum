plik = open('cyfra_kodkreskowy.txt','r')
cyfry = plik.readlines()
plik2 = open('kody.txt','r')
kody = plik2.readlines()

#1
print('ZADANIE 1')
for liczba in kody:
    suma_parzystych = 0
    suma_nieparzystych = 0
    liczba = liczba.strip()
    for i in range(0,len(liczba)):
        cyfra = int(liczba[i])
        if (i+1) % 2 == 0:
            suma_parzystych += cyfra
        else:
            suma_nieparzystych += cyfra
    print(suma_parzystych, suma_nieparzystych)

#2
print('ZADANIE 2')
def cyfra_kontrolna(liczba):
    suma_parzystych = 0
    suma_nieparzystych = 0
    liczba = liczba.strip()
    for i in range(0, len(liczba)):
        cyfra = int(liczba[i])
        if (i + 1) % 2 == 0:
            suma_parzystych += cyfra
        else:
            suma_nieparzystych += cyfra
    suma = 3*suma_parzystych + suma_nieparzystych
    wynik = suma % 10
    wynik = 10 - wynik
    wynik = wynik % 10
    for tekst in cyfry:
        if int(tekst.strip().split('\t')[0]) == wynik:
            return tekst.strip().split('\t')[1]

for i in kody:
    i = i.strip()
    cyfra_wynikowa = cyfra_kontrolna(i)
    for j in cyfry:
        x = j.strip().split('\t')[1]
        if x == cyfra_wynikowa:
            print(j.strip().split('\t')[0],cyfra_wynikowa)

#3
print('ZADANIE 3')
def kod(n,liczba_kontrolna):
    kod ='11011010'
    for cyfra in n:
        for tekst in cyfry:
            if int(tekst.strip().split('\t')[0]) == int(cyfra):
                 kod += tekst.strip().split('\t')[1]
    kod += liczba_kontrolna
    kod += '11010110'
    return kod
for i in kody:
    x = i.strip()
    liczba_kontrolna = cyfra_kontrolna(x)
    wynik = kod(x,liczba_kontrolna)
    print(wynik)

