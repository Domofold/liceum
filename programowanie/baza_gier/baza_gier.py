import ast
menu = '****************************************\nMENU:\n1.Wyświetl nazwę wszystkich gier\n2.Wyświetl wszystkie gry w bazie\n3.Wyświetl TOP 5 gier w bazie\n4.Wyświetl gry z gatunku\n5.Dodaj grę do bazy\n6.Edytuj grę w bazie\n7.Usuń grę z bazy\n8.Wyświetl informacje o grze\n9.Oceń grę\n10.Zapisz dane do pliku\n11.Odczytaj dane z pliku\n12.Zakończ\n****************************************'
gatunki_operacja_4 = []
ocena_graczy = 0.0
gatunki = []
top5 = []
oceny = []
tytuły = []
baza_gier = []
operacja = 0
while operacja != 12:
    print(menu)
    operacja = int(input('Proszę wybrać opcję: '))
    if operacja == 1:
        for gra in sorted(tytuły):
            print(gra)
    if operacja == 2:
        for gra in sorted(tytuły):
            print('\n')
            for słownik in baza_gier:
                if słownik['Tytul'] == gra:
                    for key in słownik.keys():
                        print(key, ':', słownik[key])
    if operacja == 3:
        oceny.sort(reverse=True)
        ilość = 0
        if len(oceny) > 0:
            for ocena in oceny:
                indeks = 0
                for słownik in baza_gier:
                    if ilość == 5:
                        break
                    elif baza_gier[indeks]['Ocena graczy'] != ocena:
                        indeks += 1
                    elif baza_gier[indeks]['Tytul'] in top5:
                        indeks += 1
                        continue
                    else:
                        print('\n')
                        for klucz in baza_gier[indeks].keys():
                            print(klucz, ':', baza_gier[indeks][klucz])
                        top5.append(baza_gier[indeks]['Tytul'])
                        indeks += 1
                        ilość += 1
            top5.clear()
        else:
            print('Brak ocenionych gier.')
    if operacja == 4:
        poszukiwany = input('Proszę podać gatunek: ')
        if poszukiwany in gatunki:
            for gatunek in gatunki:
                if gatunek in gatunki_operacja_4:
                    continue
                elif gatunek == poszukiwany:
                    for słownik in baza_gier:
                        if słownik['Gatunek'] == poszukiwany:
                            print(słownik['Tytul'])
                            gatunki_operacja_4.append(poszukiwany)
            gatunki_operacja_4.clear()
        else:
            print('Brak gier z podanego gatunku.')
    if operacja == 5:
        tytuł = input('Tytuł gry: ')
        tytuły.append(tytuł)
        słownik = {}
        słownik['Tytul'] = tytuł
        rok_wydania = int(input('Rok wydania: '))
        słownik['Rok wydania'] = rok_wydania
        gatunek = input('Gatunek: ')
        słownik['Gatunek'] = gatunek
        gatunki.append(gatunek)
        ocena_graczy = float(input('Ocena graczy: '))
        słownik['Ocena graczy'] = ocena_graczy
        oceny.append(ocena_graczy)
        baza_gier.append(słownik)
    if operacja == 6:
        edytowana = input('Gra którą chcesz edytować: ')
        if edytowana in tytuły:
            for słownik in baza_gier:
                if słownik['Tytul'] == edytowana:
                    edytowany_rok = int(input('Rok wydania: '))
                    słownik['Rok wydania'] = edytowany_rok
                    edytowany_gatunek = input('Gatunek: ')
                    gatunki.remove(słownik['Gatunek'])
                    gatunki.append(edytowany_gatunek)
                    słownik['Gatunek'] = edytowany_gatunek
        else:
            print('Podana gra nie istnieje w bazie.')
    if operacja == 7:
        usuń = input('Gra, którą chcesz usunąć z bazy: ')
        if usuń in tytuły:
            for słownik in baza_gier:
                if słownik['Tytul'] == usuń:
                    tytuły.remove(usuń)
                    oceny.remove(słownik['Ocena graczy'])
                    gatunki.remove(słownik['Gatunek'])
                    baza_gier.remove(słownik)
        else:
            print('Podana gra nie istnieje w bazie.')

    if operacja == 8:
        gra = input('Gra, której informację cię interesują: ')
        if gra in tytuły:
            for słownik in baza_gier:
                if słownik['Tytul'] == gra:
                    for klucz in słownik.keys():
                        print(klucz, ':', słownik[klucz])
        else:
            print('Podana gra nie istnieje w bazie.')
    if operacja == 9:
        gra = input('Gra, którą chcesz ocenić: ')
        if gra in tytuły:
            ocena = float(input('Ocena: '))
            if 0 <= ocena <= 10:
                for słownik in baza_gier:
                    if słownik['Tytul'] == gra:
                        słownik['Ocena graczy'] = ocena
            else:
                print('Podano nieprawidłową wartość (skala 0-10).')
        else:
            print('Podana gra nie istnieje w bazie.')
    if operacja == 10:
        baza_txt = open('gry.txt', 'w')
        for słownik in baza_gier:
            baza_txt.write(str(słownik))
            baza_txt.write('\n')
        baza_txt.close()
    if operacja == 11:
        baza_txt = open('gry.txt', 'r')
        baza_gier.clear()
        baza_jako_lista = baza_txt.readlines()
        for string in baza_jako_lista:
            słownik = ast.literal_eval(string.strip())
            baza_gier.append(słownik)
            oceny.append(słownik['Ocena graczy'])
            tytuły.append(słownik['Tytul'])
            gatunki.append(słownik['Gatunek'])
        baza_txt.close()

    if operacja < 1 or operacja > 12:
        print('Nie rozpoznano podanej operacji.')
