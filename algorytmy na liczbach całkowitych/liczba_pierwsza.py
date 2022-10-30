#zadanie 1

'''def czy_pierwsza(x):
    if x <= 1:
        return False
    else:
        for dzielnik in range(2,x):
            if x % dzielnik == 0:
                return False
        return True

print(czy_pierwsza(49))'''

#zadanie 2

'''def czy_pierwsza(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    pierwiastek = x**(1/2) + 1
    for dzielnik in range(3, round(pierwiastek + 1), 2):
        if x % dzielnik == 0:
            return False
    return True
print(czy_pierwsza(85))'''

#zadanie 3

'''def znajdz_liczby_pierwsze(zakres):
    T=[]
    if zakres <= 1:
        return T
    if zakres == 2:
        T.append(2)
    if zakres >= 3:
        T.append(2)
        T.append(3)
    for liczba in range(3,zakres + 1,2):
        n = 0
        for dzielnik in range(3, zakres, 2):
            if liczba % dzielnik == 0:
                n += 1
                break
            n += 1
            if n == liczba // 2 - 1:
                T.append(liczba)
                break
    return T
print(znajdz_liczby_pierwsze(100))'''

#inna implementacja

def zakres_liczby_pierwsze(zakres):
    pierwsze = []
    for liczba in range(2,zakres):
        for liczba_pierwsza in pierwsze:
            if liczba % liczba_pierwsza == 0:
                break
        else:
            pierwsze.append(liczba)
    return pierwsze
print(zakres_liczby_pierwsze(100))




