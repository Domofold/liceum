#zadanie 2
'''def czy_B_narcystyczna(x,B):
    liczba = x
    w_systemieB = []
    suma = 0
    while liczba > 0:
        if liczba % B == 0:
            liczba = liczba // B
            w_systemieB.append(0)
        if liczba % B != 0:
            w_systemieB.append(liczba % B)
            liczba = liczba // B
    w_systemieB.reverse()
    for cyfra in w_systemieB:
        suma += cyfra**len(w_systemieB)
    if suma == x:
        return 'TAK'
    else:
        return 'NIE'
print(czy_B_narcystyczna(4890,5))'''

#zadanie 4

"""def schemat_hornera(n,x,wspolczynniki):
    y = x * x
    w = wspolczynniki[len(wspolczynniki) - 1]
    for k in range(n-1,-1):
        w = y * w + wspolczynniki[k]
    return w """

#zadanie 6
??
def pierwiastek_calkowity(x,n):
    if n == 0:
        xi = x / 2
        n += 1
    p = xi // 1
    if p**2 <= xi and (p+1)**2 > xi:
        return p
    else:
        xi = (xi + x / xi) / 2
        return pierwiastek_calkowity(xi)
print(pierwiastek_calkowity(21))
??