def liste_vecteurs(n):
    V = []
    a = True
    i = 0
    j = 0
    for i in range(n):
        q = n//2
        r = n%2
        V += [r]
        n = q
        i += 1
    while a == True :
        V[i][j] = V[i][j] >> (n - j)
        j += 1
        if V[i][j]&1 == 1:
            a = False
        i += 1
    return V

n = 3
print(liste_vecteurs(n))
