plik = open('punkty.txt','r')
wiersze = plik.readlines()

#1
print('ZADANIE 1')
def czy_pierwsza(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3,n//2+1,2):
        if n % i == 0:
            return False
    return True
ile_punktow = 0
for wiersz in wiersze:
    wiersz = wiersz.strip()
    x = int(wiersz.split(' ')[0])
    y = int(wiersz.split(' ')[1])
    if czy_pierwsza(x) and czy_pierwsza(y):
        ile_punktow += 1
print(f'takich punktów jest {ile_punktow}')

#2
ile_cyfropodobnych = 0
print('ZADANIE 2')
def czy_cyfropodobne(a,b):
    A = set()
    B = set()
    for cyfra in a:
        A.add(cyfra)
    for cyferka in b:
        B.add(cyferka)
    X = list(A)
    X.sort()
    Y = list(B)
    Y.sort()
    if X == Y:
        return True
for wiersz in wiersze:
    wiersz = wiersz.strip()
    x = wiersz.split(' ')[0]
    y = wiersz.split(' ')[1]
    if czy_cyfropodobne(x,y):
        ile_cyfropodobnych += 1
print(f'jest {ile_cyfropodobnych} takich punktów')
#3
import math
print('ZADANIE 3')
max = 0
a = []
b = []
for i in range(0,len(wiersze)-1):
    wiersz = wiersze[i].strip()
    p = [int(wiersze[i].strip().split(' ')[0]),int(wiersze[i].strip().split(' ')[1])]
    for j in range(i+1,len(wiersze)):
        q = [int(wiersze[j].strip().split(' ')[0]),int(wiersze[j].strip().split(' ')[1])]
        odl = math.ceil(math.dist(p,q))
        if odl > max:
            max = odl
            a = p
            b = q
print(f'wspolrzedne punktow: A: {a}  B: {b}\nodleglosc od punktow: {max}')
#4
print('ZADANIE 4')
'''
a - wewnątrz kwadratu
b - na bokach kwadratu
c - na zewnątrz kwadratu'''
ile_a = 0
ile_b = 0
ile_c = 0
def czy_a(x,y):
    if y < 5000 and y > -5000 and x>-5000 and x < 5000:
        return True
def czy_b(x, y):
    if (x == 5000 and y <= 5000 and y>= -5000) or (x == -5000 and y <= 5000 and y >= -5000) or (y == 5000 and x <= 5000 and x >= -5000) or (y == -5000 and x <= 5000 and x >= -5000):
        return True
for wiersz in wiersze:
    wiersz = wiersz.strip()
    x = int(wiersz.split(' ')[0])
    y = int(wiersz.split(' ')[1])
    if czy_a(x,y):
        ile_a += 1
    elif czy_b(x,y):
        ile_b += 1
    else:
        ile_c += 1
print(f'a: {ile_a}\nb: {ile_b}\nc: {ile_c}')
