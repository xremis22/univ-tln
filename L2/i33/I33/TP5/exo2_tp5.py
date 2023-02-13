#def decimal_to_binaire(k):
#    L_d_b = []
#    if k == 0:
#        return 2
#    else:
#        while k != 0:
#            q = k//2
#            r = k%2
#            L_d_b += [r]
#            k = q
#    return L_d_b


def combinaison_lineaire(c,V):
    s = 0
    i = len(V)-1
    while c > 0 :
        if c&1 == 1:
            s = s ^ V[i]
        c = c >> 1
        i -= 1
    return s

c = 12
V = [ 1, 6, 3, 2 ]
print(combinaison_lineaire(c, V))
