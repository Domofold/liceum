#zadanie 2
import math
zbior = [15, 3, 2,100, 100, 10, 1, 5, 8, 6, 9, 7, 13]
max = -math.inf
max_2 = -math.inf

def znajdz_max_i_max_2(tablica, max, max_2, lewy, prawy):
    if lewy == prawy:
        if zbior[lewy] > max:
            max_2 = max
            max = zbior[lewy]
        if max > zbior[lewy] > max_2:
            max_2 = zbior[lewy]
        return max, max_2
    if prawy - lewy == 1:
        if zbior[lewy] > max:
            max_2 = max
            max = zbior[lewy]
        if zbior[prawy] > max:
            max_2 = max
            max = zbior[prawy]
        if max > zbior[lewy] > max_2:
            max_2 = zbior[lewy]
        if max > zbior[prawy] > max_2:
            max_2 = zbior[prawy]
        return max, max_2
    srodek = (lewy + prawy) // 2
    max,max_2 = znajdz_max_i_max_2(tablica, max, max_2, lewy, srodek)
    max,max_2 = znajdz_max_i_max_2(tablica, max, max_2, srodek + 1, prawy)
    return max, max_2

print(znajdz_max_i_max_2(zbior, max, max_2, 0, len(zbior) - 1))



