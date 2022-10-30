#zadanie 1
#def suma_liczb_nieparzystych(n):
#    if n % 2 == 1:
#        if n == 1:
#            return 1
#        return n + suma_liczb_nieparzystych(n-1)
#    return suma_liczb_nieparzystych(n-1)
#print(suma_liczb_nieparzystych(100))

#zadanie 2
def suma_ciagu(n):
    if n == 1:
        return 2
    else:
        return suma_ciagu(n-1)**2
print(suma_ciagu(5))