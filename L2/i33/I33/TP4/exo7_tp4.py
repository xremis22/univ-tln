def is_primitif(P):
    degree_poly = len(P)
    nbr_elem = (1 << degree_poly) - 1
    div = decompose(nbr_elem)
    i = 0
    while i < len(div):
        exp = nbr_elem/div[i]
        res = 1
        j = 0
        while j < exp:
            res = multiplie(res, 2, P)
            j += 1
        if res == 1:
            return False
        i += 1
    return True
