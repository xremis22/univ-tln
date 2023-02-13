def somme_pair(L) :
    i = 0
    cpt = 0
    while(i<len(L)):
        if(L[i]%2==0):
            cpt += L[i]
        i += 1
    return(cpt)
    
