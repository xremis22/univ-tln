def hammingweight(n) :
    cpt = 0
    L = []
    while n != 0 :
        L = [n & 1] + L
        cpt += n & 1
        n = n>>1
    return cpt

print(hammingweight(25))
