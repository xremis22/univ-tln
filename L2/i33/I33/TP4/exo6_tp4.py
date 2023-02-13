def is_irreductible(P,p):
    i = 0
    eval = 1
    while (i+1) < p and eval :
        eval = (P[0]*i + P[1])%p
        j = 2
        while j < len(P) :
            eval = (eval*i + P[j])%p
            j += 1
        i += 1
    return bool(eval)
