def funkcja(x):
    return x**2 - 4*x - 6

def poszukiwanie(l,p,epsilon):
    if funkcja(l) == 0:
        return l
    if funkcja(p) == 0:
        return p
    while p - l > epsilon:
        srodek = (l + p) / 2
        if funkcja(srodek) == 0:
            return srodek
        if funkcja(l) * funkcja(srodek) < 0:
            p = srodek
        else:
            l = srodek
    return (l + p) / 2

print(poszukiwanie(0, 20, 0.001))


def funkcja2(x):
    return 2*x**3 + 2

def poszukiwania2(l, p, epsilon):
    if funkcja2(l) == 0:
        return l
    if funkcja2(p) == 0:
        return p
    while p - l > epsilon:
        srodek = (p + l) / 2
        if funkcja2(srodek) == 0:
            return srodek
        if funkcja2(l) * funkcja2(srodek) < 0:
            p = srodek
        else:
            l = srodek
    return (l + p) / 2

print(poszukiwania2(-10,10,0.001))