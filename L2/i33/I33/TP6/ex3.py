import random

def gentrianginf(n,t):
    L = []
    for i in range(n):
        sousL = [0]*n
        for j in range(i+1):
            sousL[j] = random.randrange(0,t)
        L.append(sousL)
    return L
