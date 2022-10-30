#zadanie 1

'''def inny_na_dec(x,system):
    potega = 0
    wynik = 0
    x = str(x)
    for i in range(len(x) - 1, -1, -1):
        if int(ord(x[i])) >= 65:
            wynik += int(int(ord(x[i])) - 55) * system ** potega
            potega += 1
            continue
        wynik += int(x[i]) * system ** potega
        potega += 1
    return wynik

print(inny_na_dec(321,4))'''

#zadanie 2

def na_decy(x, system):
    potega = 0
    wynik = 0
    for cyfra in range(int(len(str(x))) - 1, -1, -1):
        if int(ord(str(x)[cyfra])) >= 65:
            wynik += (int(ord(str(x)[cyfra])) - 55) * potegowanie(system, potega)
            potega +=1
        else:
            wynik += int(str(x)[cyfra]) * potegowanie(system, potega)
            potega += 1
    return wynik

def potegowanie(liczba, potega):
    s = 1
    for i in range(0, potega):
        s *= liczba
    return s
print(na_decy(100011,2))