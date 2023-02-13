def combinaison_lineaire(c,V,p):
    L = []
    for i in range(len(V[0])):
        s = 0
        for j in range(len(c)):
            s += c[j] * V[j][i]
        L += [s%p]
    return L

p = 5
c = [2, 2, 3]
V = [[2,3,4,1], [1,1,0,2], [3,2,1,1]]

print(combinaison_lineaire(c,V,p))
