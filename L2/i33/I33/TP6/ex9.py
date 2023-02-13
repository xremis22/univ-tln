import random

def multbyalpha(b,f):
	y = b << 1
    t = (len(bin(f))-3)
    if ((y & (1 << t)) != 0):
        y = y ^ f
    return y

def table_log(P):
    Llog = [-1, 0, 1]
    r = len(bin(P)) - 3
    elem = (1 << r) - 3
    j = 0
    while j < elem :
        Llog.append(0)
        j += 1
    i = 1
    exp = 1
    while i < elem + 2:
        exp = multbyalpha(exp,P)
        Llog[exp] = i
        i += 1
    return Llog

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

def multiplie(x,y,P):
    m = len(bin(P)[3:])
    if (x==0) or (y==0):
        return 0
    log_table = table_log(P)
    alpha_table = table_alpha(P)
    indice = (log_table[x] + log_table[y]) % ((1 << m) - 1)
    return alpha_table[indice]


def matmat(A,B,P):
    x = []
    for i in range(len(A)):
        L = []
        for j in range((len(B[0]))):
            s = 0
            for k in range(len(B)):
                s = s^multiplie(A[i][k],B[k][j],P)
            L.append(s)
        x.append(L)
    return x

print(matmat([[97, 31, 46, 7, 122], [18, 75, 2, 43, 36], [47, 68, 35, 93, 68], [23, 26, 105, 65, 86], [38, 74, 122, 66, 100]],[[88, 85, 76, 81, 40], [47, 91, 75, 124, 98], [68, 91, 116, 23, 9], [9, 90, 15, 126, 53], [104, 65, 122, 24, 18]],131))

#NE FAIT PAS PARTIE DU TP
def genmatrix_inv(n) :
    M = [0]*n
    i = 0
    while i < n :
        M[i] = [0]*n
        j = 0
        while j < n :
            M[i][j] = random.randrange(k)
            j += 1
        i += 1
    return M

k = 1000

#print(genmatrix_inv(4))
