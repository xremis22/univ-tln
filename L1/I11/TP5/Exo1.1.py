#Exo 1 TP5 (1)

def som_div_propres(n):
    s=1
    i=2
    while i<n:
        if n%i==0 :
            s=s+i
        i=i+1
    return s
def est_parfait(n):
    if som_div_propres(n) == n:
        return True
    else :
        return False
def affiche_parfait(k):
    i=1
    while i<2**k:
        if est_parfait(i):
            print(i)
        i=i+1
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
n=int(input())
print(som_div_propres(n))
print(est_parfait(n))
k=int(input())
affiche_parfait(k)
print(est_presque_parfait(n))
affiche_presque_parfait(k)
