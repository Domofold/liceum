def sortowanie_przez_wybor(T):
    dlugosc = len(T)
    for i in range(0, dlugosc - 1):
        min = i
        for j in range(i + 1, dlugosc):
            if T[j] < T[min]:
                min = j
        T[i], T[min] = T[min], T[i]
    return T
print(sortowanie_przez_wybor([8,6,4,3,2,1]))