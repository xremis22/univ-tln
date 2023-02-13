def recherche2(L, S, p):
    R = []
    k = 0
    while(k<len(L)-p):
        cpt = L[k]
        i = k + 1
        while(p+k >= i):
            cpt += L[i]
            i += 1
        if(cpt >= S):
            R += [k]
        k += 1
    return R
