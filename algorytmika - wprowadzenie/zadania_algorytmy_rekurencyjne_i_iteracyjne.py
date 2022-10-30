#zadanie 2

def NWD(A,n):
    n = 0
    if len(A) == 2:
        while A[n+1] != 0:
            r = A[n] % A[n+1]
            A[n] = A[n+1]
            A[n+1] = r
        return A[n]
    a = A.pop()
    NWD(A, 0)
    A.remove(0)
    A.append(a)
    NWD(A, 0)
    return A[n]
print(NWD([20,40,60,80,100], 0))

#zadanie 3

