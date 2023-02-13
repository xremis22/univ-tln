def multiplication(n1,n2) :
    R=[0]*(len(n1)+len(n2))
    retenue=0
    retenue2=0
    for i in range(len(n1)) :
        for j in range(len(n2)) :
            p=n1[i]*n2[j]
            v=p%10+retenue
            retenue=p//10
            v2=(R[j+i]+v)%10+retenue2
            retenue2=(R[j+i]+v)//10
            R[i+j]=v2
    return R
print(multiplication([7,5,3],[5,2,1]))

from time import time
from random import randrange

def time_mult_py(n,k):
    lim=10**n
    test=[]
    for i in range(k) :
        n1=randrange(lim)
        n2=randrange(lim)
        test+=[(n1,n2)]
    start=time()
    for n1,n2 in test :
        n3 = n1*n2
        end=time()
    return(end-start)

def nombre_alea(n) :
    r=[0]*n
    for i in range(len(r)) :
        r[i]randrange(10)
    return r

def time_my_mult(n,k):
    test=[]
    for i in range(k) :
        n1=nombre_alea(n)
        n2=nombre_alea(n)
        test+=[(n1,n2)]
    start=time()
