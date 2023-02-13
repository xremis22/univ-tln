def multbyalpha(b,f):
	y = b << 1
    t = len(bin(f))-3
    if ((y & (1 << t)) != 0):
        y = y ^ f
    return y
