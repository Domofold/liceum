#zadanie 1

'''def dec_na_inny(liczba, dzielnik):
    wynik = []
    wynik_dzielenia = liczba
    reszta = 0
    while wynik_dzielenia != 0:
        wynik_dzielenia = liczba // dzielnik
        reszta = liczba % dzielnik
        if reszta > 9:
            reszta = chr(55 + reszta)
        wynik.append(reszta)
        liczba = wynik_dzielenia
    wynik.reverse()
    return wynik'''

print(dec_na_inny(23,2))

def z_decymalnego_na_inny(n, system):
    liczba = []
    while n != 0:
        reszta = n % system
        n = n // system
        if reszta > 9:
            reszta = chr(55 + reszta)
        liczba.append(reszta)
    liczba.reverse()
    return liczba

print(z_decymalnego_na_inny(797, 16))

'''zadanie 2
def zadanie_2(liczba):
    T = [2,3,4,5,6,7,8,9,16,20]
    for dzielnik in T:
        print(dec_na_inny(liczba,dzielnik))
    return '-----------------------'
print(zadanie_2(110))'''