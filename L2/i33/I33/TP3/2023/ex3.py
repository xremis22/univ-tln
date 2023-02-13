def decomose(n):
    i = 3
    l = []
    if(n%2==0):
        l += [2]
        while(n%2==0):
            n //= 2
    while(n!=1):
        if(n%i==0):
            l += [i]
            while(n%i==0):
                n//=i
        i += 2
    return l
