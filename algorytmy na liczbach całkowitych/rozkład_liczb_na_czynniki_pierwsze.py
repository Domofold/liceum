import math
#zadanie 1
'''def rozklad_na_czynniki(x):
    dzielnik = 2
    while x > 1 and dzielnik <= math.sqrt(x):
        while x % dzielnik == 0:
            print(dzielnik)
            x = x / dzielnik
        dzielnik += 1
    if x > 1:
        (print(int(x)))
    return '-'
print(rozklad_na_czynniki(17))'''

#zadanie 2

'''T = set()
tablica = []
def rozklad(x):
    dzielnik = 2
    while x > 1 and dzielnik <= math.sqrt(x):
        while x % dzielnik == 0:
            T.add(dzielnik)
            x = x / dzielnik
        dzielnik += 1
    if x > 1:
        T.add(int(x))
    for liczba in T:
        tablica.append(liczba)
    return tablica

print(rozklad(1512))'''