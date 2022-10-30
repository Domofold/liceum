#1
print('ZADANIE 1')
def fibonacci(n):
    f0 = 0
    f1 = 1
    fi = 0
    for i in range(1,n + 1):
        if i == 0 or i == 1:
            fi = i
        else:
            fi = f1 + f0
            f0 = f1
            f1 = fi
    return fi

print(f'F10: {fibonacci(10)}\nF20: {fibonacci(20)}\nF30: {fibonacci(30)}\nF40: {fibonacci(40)}')

#2
print('ZADANIE 2')
def czy_pierwsza(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for dzielnik in range(3,int((n/2)+1),2):
        if n % dzielnik == 0:
            return False
    return True
for i in range(1,41):
    if czy_pierwsza(fibonacci(i)):
        print(fibonacci(i))

#3
print('ZADANIE 3')
for i in range(1,41):
    print(bin(fibonacci(i))[2:])

#4
print('ZADANIE 4')
for i in range(1,41):
    wyraz = bin(fibonacci(i))[2:]
    ile_jedynek = 0
    for j in wyraz:
        if j == '1':
            ile_jedynek += 1
    if ile_jedynek == 6:
        print(wyraz)
