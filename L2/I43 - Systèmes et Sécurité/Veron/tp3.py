import random


def gen_cle(n) :
    L = []
    i = 0
    j = random.randrange(n-1)
    while i < n :
        L.append(i+1)
        i += 1
    n = n-1
    while n > 0 :
        L[j], L[n] = L[n], L[j]
        n -= 1
    return L

#L = [1,2,3,4,5,6]

#print(gen_cle(6))


def chiffre(clair, L):
    i = 0
    j = 0
    k = ['']*len(L)
    D = dict()
    D['à'] = 'a'
    D['é'] = 'e'
    D['è'] = 'e'
    D['ù'] = 'u'
    D['â'] = 'a'
    D['ê'] = 'e'
    D['î'] = 'i'
    D['ô'] = 'o'
    D['û'] = 'u'
    D['ä'] = 'a'
    D['ë'] = 'e'
    D['ï'] = 'i'
    D['ö'] = 'o'
    D['ü'] = 'û'
    D['ç'] = 'c'

    for x in range(ord('a'), ord('z') + 1) :
        D[chr(x)] = chr(x)
        D[chr(x).upper()] = chr(x)

    while i < len(clair) :
        let = clair[i]
        if let in D :
            let = let.lower()
            let = D[let]
            k[L[j]-1] = let
            j += 1
        i += 1
    ch = ''
    return ch.join(k)

#clair = 'Le thé est prêt'
#clair = ['L','e',' ','t','h','e',' ','e','s','t', ' ', 'p','r', 'ê', 't']
#cle = [12,11,10,9,8,7,6,5,4,3,2,1]

#print(chiffre(clair, cle))


def dechiffre(cryptogramme, L) :
    ch = ''
    i = 0
    m = ['']*len(cryptogramme)
    while(i < len(cryptogramme)) :
        m[i] = cryptogramme[L[i]-1]
        i+=1
    return ch.join(m)


#print(dechiffre('mrsuetepteqsegsunrsyesodneieeatdtnlmunuoelpuonss',[24, 30, 17, 15, 44, 38, 14, 2, 23, 39, 43, 41, 9, 45, 4, 22, 42, 10, 3, 28, 35, 5, 36, 7, 46, 31, 48, 8, 40, 47, 12, 13, 32, 21, 25, 33, 37, 34, 19, 20, 1, 29, 6, 18, 27, 11, 16, 26]))

def list_to_mat(L) :
    n = len(L)
    mat = [0]*n
    i = 0
    j = 0
    while(i < n) :
        mat[i] = [0]*n
        j += L[i] - 1
        mat[i][j] = 1
        print(mat)
        j = 0
        i += 1
    return mat


print(list_to_mat([5, 3, 2, 4, 1]))
