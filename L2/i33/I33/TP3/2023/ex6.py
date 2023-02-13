def sous_groupe_gen_mult(a, n):
    l = []
    c = a
    l += [a]
    while(c%n!=1):
        c *= a
        l += [c%n]
    return l
