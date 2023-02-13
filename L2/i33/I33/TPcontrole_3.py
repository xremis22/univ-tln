\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
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

def gentrianginf(n,t):
    L = []
    for i in range(n):
        sousL = [0]*n
        for j in range(i+1):
            sousL[j] = random.randrange(0,t)
        L.append(sousL)
    return L

def transpose(M):
    L = []
    for i in range(len(M[0])):
        sousL = []
        for j in range(len(M)):
            sousL.append(M[j][i])
        L.append(sousL)
    return L

def gentriangsup(n,t):
    L = transpose(gentrianginf(n,t))
    return L
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#ex 1 :
def is_LU(A,L,U):
    n = len(L)
    cpt0 = 0
    cpt1 = 0

    for i in range(n):
        for j in range(i+1, n):
            if L[i][j] == 0:
                cpt0 += 1

    K = gentrianginf(n,t)
    for i in range(len(K)):
        for j in range(i+1, len(K)):
            if K[i][j] == 0:
                cpt1 += 1
    if cpt0 == cpt1 :
        return True
    else :
        return False
    if False :
        break

    cpt0 = 0
    cpt1 = 0
    m = len(U)
    for i in range(m):
        for j in range(i+1, m):
            if U[i][j] == 0:
                cpt0 += 1

    T = gentriangsup(n,t)
    for i in range(len(T)):
        for j in range(i+1, len(T)):
            if T[i][j] == 0:
                cpt1 += 1
    if cpt0 == cpt1:
        return True
    else :
        return False
    if False:
        break

    F = matmat(L,U)
    if A == F:
        return True
    else :
        return False

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

            '''if L[i][j] != 0 :
                return False
    return True

    for i in range(n):
        for j in range(i+1, n):
            '''
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#ex2 :

def det(A):
    a_piv = 1
    for i in range(len(A)):
        piv = A[i][i]
        if piv == 0 :
            i_piv = i
            while piv == 0 and i_piv < len(A) :
                piv = A[i_piv][i]
                i_piv += 1
            if piv == 0:
                return 0
            else :
                cpt = A[i]
                A[i] = A[i_piv-1]
                A[i_piv-1] = cpt
                a_piv *= -1

        for j in range(i+1, len(A)):
            a_piv *= piv
            piv2 = A[j][i]
            A[j][i] = piv * piv2 - piv2 *  piv

            for  k in range(i+1, len(A)):
                A[j][k] = piv * A[j][k] - piv2 * A[i][k]

    det = 1
    for i in range(len(A)):
        det *= A[i][i]
    return det/a_piv


def est_inversible(L,U):
    K = matmat(L,U)






L = [[0, 2, 1], [4, 0, 0], [0, 0, 0]]

def determinant(L,U):
    n = len(L)
    for i in range(1, n):
        det = L[i][i]*U[i][i]
        if det = 0 :
            return True
        else :
            return False
            


print(is_LU(L))
'''B = [0.5, -0.25, 0.0], [-0.5, 0.5, 0.0], [-0.125, 0.0, 0.25]'''
