import random

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

print(gentriangsup(4,7))
