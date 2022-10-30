def sortowanie_babelkowe(T):
    dlugosc = len(T)
    for i in range (0, dlugosc - 1):
        for j in range(0, dlugosc - i - 1):
            if T[j] < T[j + 1]:
                T[j], T[j+1] = T[j+1], T[j]
    return T

print(sortowanie_babelkowe([1,2,3,4,5,6]))