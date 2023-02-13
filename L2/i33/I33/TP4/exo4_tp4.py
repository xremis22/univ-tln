def table_alpha(P) :
    m = len(bin(P)) - 3
    cardinal = (1 << m)
    L = [-1]*(cardinal)
    z = 1
    j = 0
    while j < cardinal -1 :
        L[z] = j
        z = multbyalpha(z,P)
        j += 1
    return L
