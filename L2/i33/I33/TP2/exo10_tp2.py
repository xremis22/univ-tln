#Ordre dans (Z/pZ)*

def ordre(a,p) :
    if (a == 1) :
        return 1
    i = 2
    g = False
    m = p-1
    while (i*i <= (p-1) and not(g)) :
        if ((p-1)%1 == 0) :
            r = i
            g = (pow(a,r,p) == 1)
            if not(g) :
                ter = (p-1)//i
                if (pow(a,ter,p) == 1) and (m > ter) :
                    m = ter
        i += 1
    if not(g) and m != p-1 :
        return m
    elif not(g):
        return p - 1
    else :
        return r

print(ordre(2, 7))
