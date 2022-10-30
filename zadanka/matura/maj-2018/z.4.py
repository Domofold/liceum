plik = open('sygnaly.txt','r')
wiersze = plik.readlines()

#1
print('ZADANIE 1')
przeslanie = ''
for i in range(39,len(wiersze),40):
    wiersz = wiersze[i].strip()
    przeslanie += wiersz[9]
print(f'przeslanie: {przeslanie}')

#2
print('ZADANIE 2')
szukane_slowo = ''
ilosc_roznych_liter = 0
for wiersz in wiersze:
    wiersz = wiersz.strip()
    A = set()
    for litera in wiersz:
        A.add(litera)
    if len(A) > ilosc_roznych_liter:
        szukane_slowo = wiersz
        ilosc_roznych_liter = len(A)
print(f'slowo: {szukane_slowo}\nilosc roznych liter: {ilosc_roznych_liter}')

#3
print('ZADANIE 3')
def czy_oddalona_max_o_10_slow(napis):
    napis = napis.strip()
    for i in range(0,len(napis)-1):
        for j in range(i+1,len(napis)):
            if abs(ord(napis[i]) - ord(napis[j])) > 10:
                return False
    return True
for wiersz in wiersze:
    if czy_oddalona_max_o_10_slow(wiersz):
        print(wiersz.strip())



