def najdluzszy_ciag_znakow_w_slowie_wraz_z_dlugoscia(slowo):
    obecna_litera = slowo[0]
    dlugosc = 1
    wystapienia = 1
    wynik = (obecna_litera * dlugosc, dlugosc)
    for i in range(1, len(slowo)):
        if obecna_litera == slowo[i]:
            wystapienia += 1
        else:
            wystapienia = 1
            obecna_litera = slowo[i]
        if wystapienia > dlugosc:
            dlugosc = wystapienia
            wynik = (obecna_litera * dlugosc, dlugosc)
    return wynik
print(najdluzszy_ciag_znakow_w_slowie_wraz_z_dlugoscia('aaaagbbbbbbb'))