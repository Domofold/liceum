import math

#zadanie 1

import math
def sito_eratostenesa(n):
    if n < 2:
        return []
    # Uzupełnienie tablicy (o rozmiarze n) domyślnymi wartościami True
    liczby_pierwsze = [True] * (n + 1)
    # Przejście przez cały zakres wymagany do wyznaczenia liczb pierwszych
    for i in range(2, int(math.sqrt(n)) + 1):
         # W przypadku znalezienie liczby pierwszej należy
         # wykreślić wszystkie jej wielokrotności
         if liczby_pierwsze[i]:
             for j in range(2 * i, n + 1, i):
                 # Wykreślanie odbywa się poprzez przypisanie wartości False
                 liczby_pierwsze[j] = False
    return liczby_pierwsze

sito = sito_eratostenesa(100)
liczby_pierwsze = []
for i in range(2, len(sito)):
    if sito[i]:
        liczby_pierwsze.append(i)

print(liczby_pierwsze)
print(czy_pierwsza(67))























'''def sito(x):
    T = []
    if x < 2:
        return T
    for i in range(0, x):
        T.append(i)
        T[i] = True
    T[0] = False
    for j in range(2, math.ceil(math.sqrt(x))):
        if T[i]:
            for l in range(2*i, x+1, i):
                T[l] = False
    return T

print(sito(100))'''