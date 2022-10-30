pin_użytkownika = '0055'
stan_konta = 1000
kurs_euro = 4.7
liczba_prób = 1
pin = input('Podaj PIN:')
opcja = 0
menu = '-----MENU-----\n1.Wyświetl stan konta\n2.Wpłać środki\n3.Wypłać środki\n4.Wyświetl stan konta w EURO\n5.Zakończ'
while opcja != 5 and liczba_prób != 3:
    if pin == pin_użytkownika:
        print(menu)
        opcja = float(input('Wybierz opcję:'))
        if opcja == 1:
            print('\nStan konta:', stan_konta, 'zł\n')
        if opcja == 2:
            wpłata = float(input('\nPodaj kwotę, którą chcesz wpłacić:'))
            if wpłata > 0:
                stan_konta += wpłata
                print('\nWpłacono', wpłata, 'złotych.\n')
            else:
                print('\nOperacja się nie udała, podano niepoprawną kwotę.\n',)
        if opcja == 3:
            wypłata = float(input('\nPodaj kwotę, którą chcesz wypłacić:'))
            if wypłata > 0 and wypłata <= stan_konta:
                    stan_konta -= wypłata
                    print('\nWypłacono', wypłata, 'złotych.\n')
            else:
                print('\nOperacja się nie udała, podano niepoprawną kwotę.\n')
        if opcja == 4:
            euro = stan_konta/kurs_euro
            print('\nStan konta w euro:', euro, 'euro\n')
        if opcja < 1 or opcja > 5:
            print('\nNie rozpoznano operacji. Sprawdź podany numer operacji.\n')
    else:
        liczba_prób += 1
        print('Niepoprawny PIN! Spróbuj ponownie...\nLiczba pozostałych prób:', 4-liczba_prób)
        pin = input('Podaj PIN:')

