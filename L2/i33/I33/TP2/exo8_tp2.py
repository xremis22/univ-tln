def ord(a,p):
    n = p
    while a!=0 :
        p,a=a,p%a
    return n/p
