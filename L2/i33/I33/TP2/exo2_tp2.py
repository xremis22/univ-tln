#Besoin de la fonction pgcd

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

def euclide_e(a,n):
    u=1
    v=0
    u1=0
    v1=1
    e=pgcd(a,n)
    while n!=0 :
        r = a%n
        print(r)
        q = a//n
        cp1 = u1
        cp2 = v1
        u1 = u - q * u1
        v1 = v - q * v1
        u = cp1
        v = cp2
        a = n
        n = r
    return ([u,v,a,e])

print(euclide_e(54,39))
