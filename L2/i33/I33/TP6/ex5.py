import random

def transpose(M):
    L = []
    for i in range(len(M[0])):
        sousL = []
        for j in range(len(M)):
            sousL.append(M[j][i])
        L.append(sousL)
    return L


print(transpose([[1,2,3],[4,5,6]]))
