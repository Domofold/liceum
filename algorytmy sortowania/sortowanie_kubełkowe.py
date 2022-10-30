def sortowanie_kubełkowe(A, n, max):
    # Ustalony zakres kubełków
    zakres_kubełka = 0.1
    # Obliczona liczba kubełków na podstawie największej wartości
    # oraz ustalonego wcześniej zakresu jednego kubełka.
    liczba_kubełków = int(max/zakres_kubełka)

    # Utworzenie odpowiedniej liczby kubełków. Należy dodać 1,
    # ponieważ funkcja range pominęłaby ostatni potrzebny nam kubełek.
    kubełki = []
    for i in range(liczba_kubełków + 1):
        kubełki.append([])

    # Umieszczenie liczb w odpowiednich kubełkach
    for i in range(n):
        kubełek_indeks = int(A[i]/zakres_kubełka)
        kubełki[kubełek_indeks].append(A[i])

    # Sortowanie liczb wewnątrz poszczególnych kubełków
    for i in range(liczba_kubełków + 1):
        kubełki[i].sort()

    # Umieszczanie liczb na odpowiednich, ostatecznych pozycjach
    posortowany_indeks = 0
    posortowany_kubełek = 0
    for i in range(len(kubełki)):
        for j in range(len(kubełki[i])):
            A[posortowany_indeks] = kubełki[i][j]
            # Zwiększamy indeks elementu w wyjściowej tablicy,
            # do którego przypiszemy następną posortowaną liczbę.
            posortowany_indeks += 1

     return A