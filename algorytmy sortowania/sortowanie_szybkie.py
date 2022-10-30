def ustawianie_wzgledem_osi(A, lewy, prawy):
    os = A[prawy]
    i = lewy - 1
    for j in range(lewy, prawy):
        if A[j] < os:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[prawy] = A[prawy], A[i + 1]
    return i + 1
def sortowanie_szybkie(A, lewy, prawy):
    if lewy < prawy:
        poprawny_index = ustawianie_wzgledem_osi(A, lewy, prawy)
        sortowanie_szybkie(A, lewy, poprawny_index - 1)
        sortowanie_szybkie(A, poprawny_index + 1, prawy)
    return A
A = [9,6,0,8,5,4,3,2,7]
print(sortowanie_szybkie(A, 0, len(A)-1))