#zadanie 1

#def oblicz_pierwiastek(liczba, stopień_pierwiastka):
#    return (liczba) ** (1 / stopień_pierwiastka)
#print(oblicz_pierwiastek(64,2))

#zadanie 2

#def oblicz_podzielenie(lista_liczb, dzielnik):
#    suma = 0
#    for liczba in lista_liczb:
#        if liczba%dzielnik==0:
#            suma+=1
#    print(suma)
#oblicz_podzielenie([1,2,3,4,5,6,7,8,9,10,11,12],7)

#zadanie 3

#def oblicz_unikalne_liczby(lista_liczb):
#    zbior = set()
#    for liczba in lista_liczb:
#        zbior.add(liczba)
#    print(len(zbior))
#oblicz_unikalne_liczby([1,2,3,3,3,4,5,6,6,7,7,8,9,1,1,1,2])

#zadanie 4

#def oblicz_liczbę_liter(tekst):
#    wielkie = 0
#    małe = 0
#    for litera in tekst:
#        if litera == ' ':
#            continue
#        if litera.isupper() == True:
#            wielkie+=1
#        else:
#            małe+=1
#    print('małe litery:', małe,'\nwielkie litery:', wielkie)
#oblicz_liczbę_liter('Jasiu Staśiu trele MORELE')

#zadanie 5

#def czy_doskonała(liczba):
#    suma = 0
#    if liczba > 0:
#        for dzielnik in range(1,liczba):
#            if liczba % dzielnik == 0:
#                suma+=dzielnik
#        if suma == liczba:
#            print('Podana liczba jest doskonała.')
#        else:
#            print('Podana liczba nie jest doskonała.')
#    else:
#        print('Podana liczba nie jest doskonała.')
#czy_doskonała(1374)


