def szyfrowanie(napis,klucz):
    klucz = klucz % 26
    zaszyfrowany = ''
    for litera in napis:
        litera = ord(litera)
        if litera + klucz > 90:
            zaszyfrowany += chr(litera + klucz - 26)
        else:
            zaszyfrowany += chr(litera + klucz)
    return zaszyfrowany

def odszyfrowywanie(napis, klucz):
    klucz = klucz % 26
    odszyfrowany = ''
    for litera in napis:
        litera = ord(litera)
        if litera - klucz < 65:
            odszyfrowany += chr(litera - klucz + 26)
        else:
            odszyfrowany += chr(litera - klucz)
    return odszyfrowany
print(szyfrowanie('ZWACGE',1))
print(odszyfrowywanie('AXBDHF', 1))
