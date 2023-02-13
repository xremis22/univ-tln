def generateurs(p):
    g = randrange(2, p-1)
    while(pow(g, (p-1)//2, p)==1):
        g = randrange(2, p-1)
    return g
