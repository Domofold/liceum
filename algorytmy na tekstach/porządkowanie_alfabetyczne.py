def porzadkowanie_alfabetyczne(T):
    dl = len(T)
    for i in range(0, dl - 1):
        for j in range(0, dl - i - 1):
            if czy_zmiana(T[j], T[j + 1]):
                T[j], T[j+1] = T[j + 1], T[j]
    return T

def czy_zmiana(s1, s2):
    dl1 = len(s1)
    dl2 = len(s2)
    if dl1 <= dl2:
        for i in range(0, dl1):
            if s1[i] > s2[i]:
                return True
            if s1[i] < s2[i]:
                return False
        return False
    if dl1 >= dl2:
        for i in range(0, dl2):
            if s1[i] > s2[i]:
                return True
            if s1[i] < s2[i]:
                return False
        return True

print(porzadkowanie_alfabetyczne(['g', 'h', 'j', 'a', 'w', 'd']))

#z.2
