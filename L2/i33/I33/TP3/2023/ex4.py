def generateurs(p):
    l = []
    g = 2
    k = decompose(p-1)
    while(g<p):
        j=0
        c=True
        while(j<len(k)and(c!=False)):
            if(pow(g, (p-1)//k[j], p)==1):
                c = False
            j += 1
        if c==True:
            l +=[g]
        g += 1
    return l
