#dla jednowystępującej dominanty
def moda(T):
    n = len(T)
    m = 0
    liczba = 0
    for i in range(0,n-1):
        lokaln_liczba = 0
        for j in range(i+1,n):
            if T[i] == T[j]:
                lokaln_liczba += 1
        if lokaln_liczba > liczba:
            m = T[i]
            liczba = lokaln_liczba
    return m
