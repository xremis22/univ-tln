def hammingweight2(n) :
        cpt = 0
        L = []
        while n != 0 :
            L = [n&(n-1)] + L
            cpt += n & 1
            n = n>>1
        return cpt
