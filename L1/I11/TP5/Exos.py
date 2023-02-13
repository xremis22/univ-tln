#Exos TP5
#Exo1
from math import *
def som_div_propres(n):
    s=1
    i=2
    while i<n:
        if n%i==0 :
            s=s+i
        i=i+1
    return s
def est_parfait(n):
    return(som_div_propres(n)==n)
def affiche_parfait(k):
    i=1
    while i<2**k:
        if est_parfait(i):
            print(i)
        i=i+1
#Exo2
def est_presque_parfait(n):
    if som_div_propres(n) == n-1:
        return True
    else:
        return False
def affiche_presque_parfait(k):
    i=1
    while i<2**k:
        if est_presque_parfait(i):
            print(i)
        i=i+1
#Exo3
def amicaux(n,m):
    return som_div_propres(n)==m and som_div_propres(m)==n
def affiche_amicaux(k):
    i=1
    while i<2**k:
        if amicaux(i,m):
            print(i,m)
        i=i+1
#Exo4
def somme(u,v):
    i=0
    while i<len(u):
        u[i]=u[i]+v[i]
        i=i+1
    return u
def mult(a,u):
    i=0
    while i<len(u):
        u[i]=u[i]*a
        i=i+1
    return u
def produit_scalaire(u,v):
    p=0
    for i in range(len(u)):
        p=p+u[i]*v[i]
#Exo5
def factorielle(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
def puissance(x,n):
    return x**n
def serie_exp(x,n):
    return puissance(x,n)/factorielle(n)

x=float(input("x = "))
#k est déjà utilisée mais on va le réutiliser.
while abs(serie_exp(x,n)-exp(x))<10**(-k):
    print(n)

n=int(input("n="))
print(som_div_propres(n))
print(est_parfait(n))
k=int(input("k="))
affiche_parfait(k)
print(est_presque_parfait(n))
affiche_presque_parfait(k)
m=int(input("m="))
print(amicaux(n,m))
affiche_amicaux(k)
a=int(input("a="))
b=int(input("b="))
u=[1,2,1,3]
v=[4,1,0,2]
print(somme(mult(a,u),mult(b,v)))

