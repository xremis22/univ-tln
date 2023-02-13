def euler_phi(n) :
    phi = 1
    i = 2
    while i < n :
        rev1 = n
        rev2 = i
        while rev2 != 0:
            rev1, rev2 = rev2, rev1%rev2
        if rev1 == 1 :
            phi += 1
        i += 1
    return phi
