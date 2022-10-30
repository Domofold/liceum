A = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
AM = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
def na_Morsea(slowo):
    szyfr = ''
    for litera in slowo:
        szyfr += AM[A.index(litera)]
        szyfr += ' '
    return szyfr
print(na_Morsea('MATURALNESZYFRY'))
def deszyfrowanie_Morsea(szyfr):
    odszyfrowany = ''
    szyfr = szyfr.strip().split(' ')
    for znak in szyfr:
        odszyfrowany += A[AM.index(znak)]
    return odszyfrowany
print(deszyfrowanie_Morsea(na_Morsea('MATURALNESZYFRY')))