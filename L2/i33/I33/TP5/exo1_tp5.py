def combinaison_lineaire(c,V):
    L = []
    for i in range(len(V[0])):
        s = 0
        for j in range(len(c)):
            s += c[j] * V[j][i]
        L += [s]
    return L


V = [[5, 9, 8, 2, 7], [1, 9, 3, 9, 3], [8, 3, 1, 2, 7], [5, 7, 3, 7, 2], [4, 1, 1, 2, 8]]
c = [2, 2, 9, 3, 6]

print(combinaison_lineaire(c,V))
