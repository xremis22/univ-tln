import random
#lorsqu'on importe une librairie, si on fait que "import ..." il faut mettre le
#nom de la librairie devant la fonction

def genmatrix(n,p,t):
    L = []
    for i in range(n):
        sousL = []
        for j in range(p):
            sousL.append(random.randrange(0,t))
        L.append(sousL)
    return L

print(genmatrix(2,3,7))
