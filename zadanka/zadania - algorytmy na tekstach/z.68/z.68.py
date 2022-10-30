plik = open('dane_napisy.txt', 'r')
napisy = plik.readlines()

#z.1
def anagramy_jednolite(s1, s2):
    if len(s1) != len(s2):
        return False
    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            return False
    return True

s = 0
for para in napisy:
    if anagramy_jednolite(para.split(' ')[0], para.split(' ')[1].strip()):
        s += 1
odp = open('wyniki_anagramy.txt', 'w')
odp.write('ZADANIE 1 \n')
odp.write(f'{s}')

#z.2

def czy_anagramy(a, b):
    if len(a) != len(b):
        return False
    T = []
    for i in range(0, 127):
        T.append(0)
    for i in range(0, len(a)):
        T[ord(a[i])] += 1
    for i in range(0, len(b)):
        T[ord(b[i])] -= 1
    for i in range(0, 127):
        if T[i] != 0:
            return False
    return True

z = 0
for para in napisy:
    if czy_anagramy(para.split(' ')[0], para.split(' ')[1].strip()):
        z += 1
odp.write('\nZADANIE 2\n')
odp.write(f'{z}')

#z.3
T = []
for para in napisy:
    if czy_anagramy(para.split(' ')[0], para.split(' ')[1].strip()):
        T.append(para.split(' ')[0])
        T.append(para.split(' ')[1].strip())
max = 0
for i in T:
    p = 0
    for para in napisy:
        if czy_anagramy(i, para.split(' ')[0]):
            p += 1
        if czy_anagramy(i, para.split(' ')[1].strip()):
            p += 1
    if p > max:
        max = p
print(max)
odp.write('\nZADANIE 3\n')
odp.write(f'{max}')

plik.close()