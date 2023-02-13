import random

def matvec(M,V):
    L = []
    for i in range(len(M)):
        s = 0
        for j in range(len(V)):
            s += M[i][j]*V[j]
        L.append(s)
    return L
    
