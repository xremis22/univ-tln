def inverse(a,p):
    u=1
    v=0
    u1=0
    v1=1
    n=p
    while p!=0 :
        r = a%p
        q = a//p
        a = p
        p = r
        rev1 = u - q * u1
        rev2 = v - q * v1
        u = u1
        v = v1
        u1 = rev1
        v1 = rev2
    return (u%n)
