plik = open('dane.txt','r')
wiersze = plik.readlines()

#1
print('ZADANIE 1')
najjasnieszy = 0
najciemniejszy = 255
for wiersz in wiersze:
    wiersz = wiersz.strip().split(' ')
    for cyfra in wiersz:
        cyfra = int(cyfra)
        if cyfra < najciemniejszy:
            najciemniejszy = cyfra
        if cyfra > najjasnieszy:
            najjasnieszy = cyfra
print(f'najjasniejszy piksel: {najjasnieszy}\nnajciemniejszy piksel: {najciemniejszy}')

#2
print('ZADANIE 2')
ile_usunac = 0
for wiersz in wiersze:
    wiersz1 = wiersz.strip()[0:int(len(wiersz.strip())/2)].split(' ')
    wiersz2 = wiersz.strip()[int(len(wiersz.strip())/2):len(wiersz.strip())].split(' ')
    wiersz2.reverse()
    if wiersz1 != wiersz2:
        ile_usunac += 1
print(f'nalezy usunac: {ile_usunac} wierszy')

#3
'''print('ZADANIE 3')
ile_kontrastujacych = 0
for i in range(0,len(wiersze)):
    for j in range(0,len(wiersze[i].strip())-1):
        wiersz = int(wiersze[i].strip().split(' ')[j])
        if abs(wiersz - int(wiersze[i].strip().split(' ')[j + 1])) > 128 or abs(wiersz - int(wiersze[i+1].strip().split(' ')[j])) > 128:
            ile_kontrastujacych += 1
        elif j != 1 and abs(wiersz - int(wiersze[i].strip().split()[j-1])) > 128:
            ile_kontrastujacych += 1
    if abs(int(wiersze[i].strip().split(' ')[len(wiersze)]) - int(wiersze[i+1].strip().split(' ')[j])) > 128:
        ile_kontrastujacych += 1

print(f'jest {ile_kontrastujacych} takich pikseli')'''

#4
print('ZADANIE 4')
max = 0
for i in range(0,len(wiersze[1].strip().split(' '))):
    max_lokal = 1
    for j in range(0,len(wiersze)-1):
        if wiersze[j].strip().split(' ')[i] == wiersze[j+1].strip().split(' ')[i]:
            max_lokal += 1
        else:
            if max_lokal > max:
                max = max_lokal
            max_lokal = 1
print(f'najdluzsza linia pionowa: {max}')




