#def det(A):
#    L1 = 0
#    L2 = 0
#    L = []
#    calc = 0
#    while (L1 <= len(A)) :
#        while (L2 <= len(A)) :
#            if L1 == L2 :
#                L[L2] = A[L1][L2]
#            L2 += 1
#        calc = L[L1] * L[L1]
#        L1 += 1
#    return calc

#A = [[3,7,5],[4,2,6],[1,10,9]]
#print(det(A))

M = [[11,7,9],[3,-2,6],[19,6,-9]]
sorted(M, key=lambda M:M[2])
print(M)

def elementmedian(M):
    i = 0
    j = 0
    n = len(M)
    N = [0]*n
    k = 0
    p = (n*n - 1)//2
#    elem = N[p-1]
    for i in range(n) :
        for j in range(n) :
            for k in range(n*n) :
                N[k] = min(M[i])
                k += 1
#    return elem

#print(elementmedian(M))


def det(A):
    a = 1
    b = 1
    p = 1
    for j in range(len(A)-1):
        k = j
        while (k < len(A)) and (A[k][j] == 0):
            k = k + 1
        if (k == len(A)):
            return 0
        if (k != j):
            A[k],A[j] = A[j], A[k]
            a = -a
        b = b * A[j][j]
        for k in range(j+1,len(A)):
            p = p * A[j][j]
            s = A[k][j]
            for c in range(0,len(A)):
                A[k][c]=A[k][c]*A[j][j]-A[j][c]*s
    b = b * A[len(A)-1][len(A)-1]*a
    if (abs(d) == 0):
        b = 0
    return(b/p)
