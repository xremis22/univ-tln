def multbyalpha(b,f):
	y = b << 1
    t = len(bin(f))-3
    if ((y & (1 << t)) != 0):
        y = y ^ f
    return y
    
def multiplication(b,c,f):
    r = 0
    t = b
    k = c
    while t != 0:
        if (t & 1) != 0:
            r ^= k
        k = multbyalpha(k,f)
        t = t >> 1
    return r

print(multiplication(5,6,13))
