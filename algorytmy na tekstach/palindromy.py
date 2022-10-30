def czy_palindrom(slowo):
    i = 0
    j = len(slowo) - 1
    while i < j:
        while slowo[i] == ' ':
            i += 1
        while slowo[j] == ' ':
            j -= 1
        if slowo[i] == slowo[j]:
            i += 1
            j -= 1
        else:
            return False
    return True
print(czy_palindrom('aabaa'))

