def sortowanie_przez_wstawianie(A):
    le = len(A)
    for i in range(1, le):
        j = i
        while j > 0 and A[j] < A[j-1]:
            A[j],A[j-1] = A[j-1], A[j]
            j -= 1
    return A

print(sortowanie_przez_wstawianie([9,8,7,6,5,4,3,2,1]))