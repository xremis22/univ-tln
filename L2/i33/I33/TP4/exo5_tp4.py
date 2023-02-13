def multiplie(x, y, P):
    r = len(bin(P)) - 2
    r2 = 1 << r
    if x == 0 or y == 0 :
        return 0
    else :
        u = log_table[x]
        v = log_table[y]
        s = (u + v)%(r2 - 1)
        return table_alpha[s]
        
