def szyfr_spolglosek(slowo):
    T = ['a','e','i','o','u','y','A','E','I','O','U','Y','ą','ę','Ą','Ę']
    i = 0
    szyfr = ''
    while i < len(slowo) - 1:
        if slowo[i] in T:
            szyfr += slowo[i + 1] + slowo[i]
            i += 2
        else:
            szyfr += slowo[i]
            i += 1
    if len(slowo) != len(szyfr):
        szyfr += slowo[len(slowo)-1]
    return szyfr
print(szyfr_spolglosek('abcdefg'))

def deszyfrowanie(slowo):
    T = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y', 'ą', 'ę', 'Ą', 'Ę']
    i = 0
    szyfr = slowo
    while i < len(slowo) - 1 and i > 0:
        if slowo[i] in T:
            szyfr[i - 1], szyfr[i] = slowo[i], szyfr[i - 1]
            i += 2
    return szyfr

print(deszyfrowanie('abcdefg'))


