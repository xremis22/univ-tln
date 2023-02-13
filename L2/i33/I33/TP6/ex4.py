import random

def gentrianginf(n,t):
    L = []
    for i in range(n):
        sousL = [0]*n
        for j in range(i+1):
            sousL[j] = random.randrange(0,t)
        L.append(sousL)
    return L

def gensym(n,t):
    L = gentrianginf(n,t)
    for i in range(n):
        for j in range(i):
            L[j][i] = L[i][j]
    return L


print(gentrianginf(4,10))
print(gensym(4,10))
