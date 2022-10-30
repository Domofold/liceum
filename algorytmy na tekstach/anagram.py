def czy_anagram(slowo1, slowo2):
    dl1 = len(slowo1)
    dl2 = len(slowo2)
    if dl1 != dl2:
        return False
    T = []
    for i in range(0, 127):
        T.append(0)
    for i in range(0, dl1):
        T[ord(slowo1[i])] = T[ord(slowo1[i])] + 1
    for i in range (0, dl2):
        T[ord(slowo2[i])] = T[ord(slowo2[i])] - 1
    for i in range(0, 127):
        if T[i] != 0:
            return False
    return True

print(czy_anagram('mat', 'mat'))

