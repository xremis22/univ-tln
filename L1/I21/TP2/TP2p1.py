#Question 2
def intervalle(a,b,inc) :
    L=[]
    i=inc
    if a < b :
        cpt=a
        while cpt <= b :
            L+=[cpt]
            cpt+=i
    elif a > b :
        cpt=b
        while cpt <= a:
            L+=[cpt]
            cpt+=i
    else :
        print("L = ", a)
    return L
print(intervalle(0,1,0.2))

#Question 3
from math import *

def valeur_sin(L) :
    liste_sin=[]
    for i in range(len(L)) :
        liste_sin+=[sin(L[i])]
    return liste_sin

def valeur_cos(L) :
    liste_cos=[]
    for i in range(len(L)) :
        liste_cos+=[cos(L[i])]
    return liste_cos

#Question 4
import matplotlib . pyplot as plt

abs= intervalle(-2*pi,2*pi,0.1)
liste_sin=valeur_sin(abs)
liste_cos=valeur_cos(abs)
plt . plot ( abs , liste_sin , abs , liste_cos )
plt . show ()
