def sommefibo(j):
    i = 2
    M = [0, 1]
    som = 1
    while(i<j):
        M += [M[i-1] + M[i-2]]
        som += M[i]
        i += 1
    if(j==0):
        return 0
    else :
        return som
