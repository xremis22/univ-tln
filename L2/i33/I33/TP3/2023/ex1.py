def generateurs(n):
    L = []
    for i in range(1, n):
        if(pgcd(n, i)==1):
            L += [i]
    return L
