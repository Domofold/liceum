plik = open('napisy.txt','r')
wiersze = plik.readlines()

#1
print('ZADANIE 1')
ile_cyfr = 0
for wiersz in wiersze:
    wiersz = wiersz.strip()
    for i in wiersz:
        if i >= '0' and i <= '9':
            ile_cyfr += 1
print(ile_cyfr)

#2
print('ZADANIE 2')
haslo =''
j = 0
for i in range(19,len(wiersze),20):
    haslo += wiersze[i].strip()[j]
    j += 1
print(haslo)

#3
print('ZADANIE 3')
def czy_palindrom(n):
    i = 0
    j =len(n)-1
    while i < j:
        if n[i] == n[j]:
            i += 1
            j -= 1
        else:
            return False
    return True
wiadomosc = ''
for wiersz in wiersze:
    wiersz = wiersz.strip()
    opcja_1 = wiersz[len(wiersz)-1] + wiersz
    opcja_2 = wiersz + wiersz[0]
    if czy_palindrom(opcja_1):
        wiadomosc += opcja_1[len(opcja_1)//2]
    if czy_palindrom(opcja_2):
        wiadomosc += opcja_2[len(opcja_2)//2]
print(wiadomosc)

#4
haselko = ''
print('ZADANIE 4')
for wiersz in wiersze:
   wiersz = wiersz.strip()
   lokal =''
   for i in wiersz:
       if i >= '0' and i <= '9':
           lokal += i
   if len(lokal) < 2:
      continue
   for j in range(0,len(lokal),2):
       o = int(lokal[j:j+2])
       if o >= 65 and o <= 90:
           haselko += chr(int(lokal[j:j+2]))
index = haselko.index('X')
print(haselko[:index+3])
