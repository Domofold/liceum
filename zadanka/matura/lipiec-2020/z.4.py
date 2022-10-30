plik = open('identyfikator.txt','r')
wiersze = plik.readlines()

#1
print('ZADANIE 1')
MAX = []
max = 0
for slowo in wiersze:
    slowo = slowo.strip()
    suma = 0
    for i in range(3,len(slowo)):
        suma += int(slowo[i])
    if suma > max:
        MAX.clear()
        max = suma
        MAX.append(slowo)
    elif suma == max:
        MAX.append(slowo)
for i in MAX:
    print(i)

#2
print('\nZADANIE 2')
def czy_palindrom(slowo):
    l = 0
    p = len(slowo) - 1
    while l < p:
        if slowo[l] == slowo[p]:
            l += 1
            p -= 1
            continue
        else:
            return False
    return True

for slowo in wiersze:
    slowo = slowo.strip()
    seria = slowo[:3]
    numer = slowo[3:]
    if czy_palindrom(seria) or czy_palindrom(numer):
        print(slowo)

#3
print('\nZADANIE 3')
def czy_niepoprawny(slowo):
    lista = list(slowo)
    suma = 0
    wagi = [7, 3, 1, 0, 7, 3, 1, 7, 3]
    for i in range(0,3):
        lista[i] = int(ord(lista[i])-55)
    for i in range(0,len(lista)):
        suma += int(lista[i]) * wagi[i]
    reszta = suma % 10
    if reszta == int(lista[3]):
        return False
    return True
for slowo in wiersze:
    slowo = slowo.strip()
    if czy_niepoprawny(slowo):
        print(slowo)
