#zadanie 1

'''def element_fibo(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    return element_fibo(x-2) + element_fibo(x-1)
#print(element_fibo(6))'''

#zadanie 2

'''def fibo_rekur(zakres):
    T = []
    for liczba in range(1, zakres + 1):
        x = element_fibo(liczba)
        if x > zakres:
            break
        T.append(x)
    return T
print(fibo_rekur(1000))'''

#zadanie 1

def fibo_iteracyjnie(n):
    f0 = 0
    f1 = 1
    fi = 0
    for liczba in range(0, n+1):
        if liczba <= 1:
            fi = liczba
        else:
            fi = f0 + f1
            f0 = f1
            f1 = fi
    return fi
print(fibo_iteracyjnie(3))

#zadanie 2

'''def fibo_iter(zakres):
    T = []
    f0 = 0
    f1 = 1
    fi = 0
    for liczba in range(1, zakres + 1):
        if liczba <= 1:
            fi = liczba
        else:
            fi = f0 + f1
            f0 = f1
            f1 = fi
            if fi > zakres:
                break
        T.append(fi)
    return T
print(fibo_iter(100))'''

