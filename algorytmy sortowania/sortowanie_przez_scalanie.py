def sortowanie_przez_scalanie(T, lewy, prawy):
    if lewy == prawy:
        return
    srodkowy = (lewy + prawy) // 2
    sortowanie_przez_scalanie(T, lewy, srodkowy)
    sortowanie_przez_scalanie(T, srodkowy + 1, prawy)
    scalanie(T, lewy, prawy, srodkowy)

def scalanie(T, lewy, prawy, srodkowy):
    prawa_strona = T[srodkowy + 1:prawy + 1]
    lewa_strona = T[lewy: srodkowy + 1]

    indeks_lewej = 0
    indeks_prawej = 0
    indeks_sortowanej = lewy

    while indeks_lewej < len(lewa_strona) and indeks_prawej < len(prawa_strona):
        if lewa_strona[indeks_lewej] < prawa_strona[indeks_prawej]:
            T[indeks_sortowanej] = lewa_strona[indeks_lewej]
            indeks_lewej += 1
        else:
            T[indeks_sortowanej] = prawa_strona[indeks_prawej]
            indeks_prawej += 1
        indeks_sortowanej += 1
    while indeks_lewej < len(lewa_strona):
        T[indeks_sortowanej] = lewa_strona[indeks_lewej]
        indeks_lewej += 1
        indeks_sortowanej += 1
    while indeks_prawej < len(prawa_strona):
        T[indeks_sortowanej] = prawa_strona[indeks_prawej]
        indeks_prawej += 1
        indeks_sortowanej += 1

T = [9,8,7,6,5,4,3,2,1]
sortowanie_przez_scalanie(T, 0 , (len(T) - 1))
print(T)



