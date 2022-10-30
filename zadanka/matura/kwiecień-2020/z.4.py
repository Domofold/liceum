plik = open('dane4.txt','r')
wiersze = plik.readlines()

#1
print('ZADANIE 1')
max = 0
min = 100000000
for i in range(0,len(wiersze)-1):
    wiersz = wiersze[i].strip()
    x = abs(int(wiersze[i+1]) - int(wiersz))
    if x > max:
        max = x
    elif x < min:
        min = x
print(f'największa luka: {max}\nnajmniejsza luka: {min}')

#2
print('ZADANIE 2')
max_długość_regularnego = 0
start_max_regularny = 0
stop_max_regularny = 0
for i in range(0, len(wiersze) - 1):
    start = int(wiersze[i])
    następny = int(wiersze[i + 1])
    luka = abs(start - następny)
    długość = 2
    for j in range(i + 2, len(wiersze)):
        if abs(int(wiersze[j - 1]) - int(wiersze[j])) != luka:
            if długość > max_długość_regularnego:
                max_długość_regularnego = długość
                start_max_regularny = start
                stop_max_regularny = int(wiersze[j - 1])
            break
        else:
            długość += 1

print(f'najwieksza dlugosc: {max_długość_regularnego}')
print(f'pierwsza liczba: {start_max_regularny}')
print(f'ostatnia liczba: {stop_max_regularny}')

#3
print('ZADANIE 3')
krotnosc = 0
krotnosc = set()
luki = set()
slownik = {}
for i in range(0,len(wiersze)-1):
    luka = abs(int(wiersze[i+1].strip()) - int(wiersze[i].strip()))
    luki.add(luka)
for i in luki:
    slownik[i] = 0
for i in range(0,len(wiersze)-1):
    luka = abs(int(wiersze[i+1].strip()) - int(wiersze[i].strip()))
    slownik[luka] += 1
print('najwieksza krotnosc = 31')
for i in slownik.keys():
    if slownik[i] == 31:
        print(i)





