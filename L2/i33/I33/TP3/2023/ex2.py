def sous_groupe_gen_add(a, n):
    L = []
    c = 0
    while(True):
        c += a
        L += [c%n]
        if((c%n)==0):
            break
    return L
