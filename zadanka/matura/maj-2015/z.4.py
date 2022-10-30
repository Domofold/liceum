plik = open('liczby.txt','r')
wiersze = plik.readlines()

#1
print('ZADANIE 1')
ile_wierszy = 0
for wiersz in wiersze:
    wiersz = wiersz.strip()
    ile_zer = 0
    ile_jedynek = 0
    for cyfra in wiersz:
        if cyfra == '1':
            ile_jedynek += 1
        if cyfra == '0':
            ile_zer += 1
    if ile_zer > ile_jedynek:
        ile_wierszy += 1
print(ile_wierszy)

#2
print('ZADANIE 2')
podzielnych_przez_2 = 0
podzielnych_przez_8 = 0
for wiersz in wiersze:
    liczba = int(wiersz.strip(),2)
    if liczba % 2 == 0:
        podzielnych_przez_2 += 1
    if liczba % 8 == 0:
        podzielnych_przez_8 += 1
print(f'podzielnych przez 2: {podzielnych_przez_2}\npodzielnych przez 8: {podzielnych_przez_8}')

#3
print('ZADANIE 3')
A = []
for wiersz in wiersze:
    liczba = int(wiersz.strip(),2)
    A.append(liczba)
maksimum = max(A)
wiersz_maksimum = A.index(maksimum) + 1
minimum = min(A)
wiersz_minimum = A.index(minimum) + 1

print(f'wiersz max: {wiersz_maksimum}\nwiersz min: {wiersz_minimum}')