import random

def gendiag(n,t):
    L = []
    for i in range(n):
        sousL = [0]*n
        sousL[i] = random.randrange(0,t)
        L.append(sousL)
    return L
