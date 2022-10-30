#zadanie 1

'''def euklides_iter(a,b):
    pom = 0
    while b != 0:
        pom = b
        b = a % b
        a = pom
    return a
#print(euklides_iter(13,197))'''

#zadanie 2

'''def znajdz_nwd_wielu_liczb(lista):
    dz = lista[0]
    for i in range(1, len(lista)):
        dz = euklides_iter(dz,lista[i])
    return dz
print(znajdz_nwd_wielu_liczb([244,1024,4024,5096,10020,17448]))'''

#zadanie 1
def euklides_rekur(a,b):
    if b != 0:
        return euklides_rekur(b,a % b)
    return a
#print(euklides_rekur(12,4))

#zadanie 2

def znajdz_nwd_wielu_liczb(lista):
    dz = lista [0]
    for i in range(1, len(lista)):
        dz = euklides_rekur(dz,lista[i])
    return dz
print(znajdz_nwd_wielu_liczb([244,1024,4024,5096,10020,17448]))