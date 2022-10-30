plik1 = open('dane_6_1.txt','r')
plik2 = open('dane_6_2.txt','r')
plik3 = open('dane_6_3.txt','r')
wiersze1 = plik1.readlines()
wiersze2 = plik2.readlines()
wiersze3 = plik3.readlines()

#1
print('ZADANIE 1')
def szyfr_Cezara(slowo,klucz):
    klucz = klucz % 26
    zaszyfrowane = ''
    for pozycja in slowo:
        if ord(pozycja) + klucz > 90:
            id = abs(90 - ord(pozycja) - klucz)
            zaszyfrowane += chr(65 + id)
        else:
            id = ord(pozycja) + klucz
            zaszyfrowane += chr(id)
    return zaszyfrowane

for wiersz in wiersze1:
    wiersz = wiersz.strip()
    print(szyfr_Cezara(wiersz,107))

#2
print('ZADANIE 2')
def deszyfrowanie(slowo,klucz):
    klucz = klucz % 26
    odszyfrowane = ''
    for litera in slowo:
        if ord(litera) - klucz < 65:
            id = abs(ord(litera) - 65 - klucz)
            odszyfrowane += chr(91 - id)
        else:
            id =ord(litera) - klucz
            odszyfrowane += chr(id)
    return odszyfrowane
for wiersz in wiersze2:
    wiersz = wiersz.strip().split(' ')
    if len(wiersz) != 2:
        continue
    wierszyk = wiersz[0]
    klucz = int(wiersz[1])
    print(deszyfrowanie(wierszyk,klucz))

#3
print('ZADANIE 3')

for wiersz in wiersze3:
    slowo = wiersz.strip().split(' ')[0]
    zaszyfrowane = wiersz.strip().split(' ')[1]
    for i in range(0,26):
        if slowo == deszyfrowanie(zaszyfrowane,i):
            break
    else:
        print(slowo)




