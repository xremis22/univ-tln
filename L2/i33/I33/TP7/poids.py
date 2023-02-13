def poids(n):
    cpt = 0
    while n != 0:
        if n & 1:
            cpt += 1
    n >> =1
    return cpt
