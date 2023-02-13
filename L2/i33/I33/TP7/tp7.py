def norme(M):
    sM = 0
    for j in range(len(M[0])):
        #sert à parcourir la colonne
        s = 0
        for i in range(len(M)):
            #sert à parcourir la ligne
            s += abs(M[i][j])
        if s > sM :
            sM = s
    return sM

def poids(n):
    cpt = 0
    while n != 0:
        if n & 1:
            cpt += 1
    n >>=1
    return cpt

def prod_mat_vect_F2(M,V):
    s = 0
    for i in range(len(M)):
        s |= poids(M[i]&V)&1
        s<<=1
    return s >> 1

def gencirculante(L):
    M = []
    for i in range(len(L)):
        l = L[len(L)-i:] + L[:len(L)-i]
        M += [l]
    return M

def circmultvec(V,Y):
    W = []
    i = 0
    while i > -len(V) :
        s = 0
        k = i
        for j in range(len(V)):
            s += V[k]*Y[j]
            k += 1
        W += [s]
        i -= 1
    return W

def gen_circulante2(k,t):
    
