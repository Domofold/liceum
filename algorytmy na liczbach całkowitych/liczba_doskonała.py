#zadanie 1

'''def czy_doskonala(x):
    dzielniki = []
    for dzielnik in range(1, int(x/2 + 1)):
        if x % dzielnik == 0:
            dzielniki.append(dzielnik)
    suma = 0
    for dzielnik in dzielniki:
        suma += dzielnik
    if suma == x:
        return True
    else:
        return False
print(czy_doskonala(8128))'''

#zadanie 2

'''def znajdz_liczby_doskonale(zakres):
    T = []
    for liczba in range(1, zakres + 1):
        if czy_doskonala(liczba):
            T.append(liczba)
    return T
print(znajdz_liczby_doskonale(20000))'''

#zadanie 3

'''def znajdz_liczby_doskonale(zakres):
    T = []
    dzielniki = []
    if zakres == 1:
        return False
    for liczba in range(2, zakres + 1, 2):
        suma = 0
        for dzielnik in range(1, int(liczba/2 +1)):
            if liczba % dzielnik == 0:
                suma += dzielnik
        if liczba == suma:
            T.append(liczba)
    return T
print(znajdz_liczby_doskonale(20000))'''




