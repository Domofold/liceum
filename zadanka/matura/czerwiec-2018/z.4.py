plik1 = open('dane1.txt','r')
plik2 = open('dane2.txt','r')
wiersze1 = plik1.readlines()
wiersze2 = plik2.readlines()

#1
print('ZADANIE 1')
ile = 0
for i in range(0,len(wiersze2)):
    if wiersze1[i].strip().split(' ')[len(wiersze1[i].strip().split(' '))-1] == wiersze2[i].strip().split(' ')[len(wiersze2[i].strip().split(' '))-1]:
        ile += 1
print(f'ostatnia liczba jest taka sama w dwoch ciagach: {ile} razy')

#2
print('ZADANIE 2')
ile2 = 0
for i in range(0,len(wiersze2)):
    parzystych1 = 0
    nieparzystych1 = 0
    parzystych2 = 0
    nieparzystych2 = 0
    w1 = wiersze1[i].strip().split(' ')
    for liczba in w1:
        if int(liczba) % 2 == 0:
            parzystych1 += 1
        else:
            nieparzystych1 += 1
    w2 = wiersze2[i].strip().split(' ')
    for liczba in w2:
        if int(liczba) % 2 == 0:
            parzystych2 += 1
        else:
            nieparzystych2 += 1
    if nieparzystych1 == 5 and nieparzystych2 == 5 and parzystych2 == 5 and parzystych1 == 5:
        ile2 += 1
print(f'par takich ciagow: {ile2}')

#3
print('ZADANIE 3')
ile_3 = 0
numery_wierszy = []
for i in range(0,len(wiersze2)):
    czy = True
    for liczba in wiersze1[i].strip().split(' '):
        if liczba in wiersze2[i].strip().split(' '):
            continue
        else:
            czy = False
    for liczba in wiersze2[i].strip().split(' '):
        if liczba in wiersze1[i].strip().split(' '):
            continue
        else:
            czy = False

    if czy:
        numery_wierszy.append(i+1)
        ile_3 += 1
print(f'par ciagow: {ile_3}\nnumery wierszy: {numery_wierszy}')

#4
print('ZADANIE 4')
for i in range(0,len(wiersze2)):
    w1 = wiersze1[i].strip().split(' ')
    w2 = wiersze2[i].strip().split(' ')
    for j in range(0,len(w1)):
        pom1 = int(w1[j])
        w1[j] = pom1
        pom2 = int(w2[j])
        w2[j] = pom2
    w = w1 + w2
    w.sort()
    for l in range(0,len(w)):
        pom1 = str(w[l])
        w[l] = pom1
    wynik = ' '.join(w)
    print(wynik)


