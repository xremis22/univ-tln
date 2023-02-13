def pgcd(a,b):
    c=0
    while b>a :
        c=a
        a=b
        b=c
    if b==0:
        return a
    else :
        reste=a%b
        return pgcd(b,reste)


def generateurs(n):
    l=[]
    for x in range(1,n):
        if pgcd(x,n)==1:
            l += [x]
    return l
print(generateurs(14))
print(generateurs(7))
print(generateurs(0))
print(generateurs(1))
