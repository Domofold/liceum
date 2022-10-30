plik = open('tekst.txt','r')
wiersz = plik.readlines()[0].split(' ')

#1
print('ZADANIE 1')
for slowo in wiersz:
    slowo = slowo.strip()
    if slowo[0] == 'd'and slowo[len(slowo)-1] == 'd':
        print(slowo)

#2
print('ZADANIE 2')
def szyfr_afiniczny(slowo,A,B):
    zaszyfrowane = ''
    for litera in slowo:
        i = (ord(litera) - 97) * A
        wynik = i + B
        if wynik > 25:
            wynik = wynik % 26
        zaszyfrowana = chr(97+wynik)
        zaszyfrowane += zaszyfrowana
    return zaszyfrowane

T = []
unikalne = set()
for i in wiersz:
    if len(i) >= 10:
        T.append(i)
for slowo in T:
    print(szyfr_afiniczny(slowo, 5, 2))

#3
print('ZADANIE 3')
plik = open('probka.txt','r')
wiersze = plik.readlines()
def szyfrujacy(slowo,szyfr):
    for i in range(0,26):
        for j in range(0,26):
            if szyfr_afiniczny(slowo,i,j) == szyfr:
                return i, j
print('szyfrujące:')
for i in wiersze:
    i = i.split(' ')
    print(f'{i[0]} {szyfrujacy(i[0],i[1].strip())}')
print('deszyfujące')
for i in wiersze:
    i = i.split(' ')
    print(f'{i[1].strip()} {szyfrujacy(i[1].strip(),i[0])}')






