def somme_ind_pair(L):
    i = 0
    cpt = 0
    while(i<len(L)):
        if(i%2==0):
            cpt += L[i]
        i += 1
    return cpt
