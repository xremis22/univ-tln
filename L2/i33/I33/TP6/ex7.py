import random

def matmat(A,B):
    prod = []
    for i in range(len(A)) :
        aux = []
        for j in range(len(B[0])) :
            somme = 0
            for k in range(len(A[0])) :
                somme += A[i][k] * B[k][j]
            aux += [somme]
        prod += [aux]
    return prod




def gentrinanginf_inv(n,t) :
    M = [0]*n
    h = 1
    i = 0
    while i < n :
        M[i] = [0]*n
        j = 0
        while j < h :
            M[i][j] = random.randrange(0,t)
            j += 1
        i += 1
        h += 1
    return M
n = 4
t = 1000
print(gentrinanginf_inv(n,t))
