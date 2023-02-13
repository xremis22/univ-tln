#TD2
#Exo4.1

a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))

if a<b<c:
    print(c)
elif a>b>c:
    print(a)
elif a<b and c<b:
    print(b)

#4.2
CT=int(input("CT = "))
CC=int(input("CC = "))
TP=int(input("TP = "))
nf=0
if CT*0.7>CT*0.5+0.2*CC:
    nf=0.3*TP+CT*0.7
else :
    nf=0.3*TP+CT*0.5+0.2*CC
print("La note finale de I11 est :",nf)

#4.3
if a==b==c:
    print("Le triangle est equilateral")
elif a==b or b==c or a==c:
    print("Le triangle est isocele")
else :
    print("Le triangle est quelconque")

#4.4
x1=0
x2=0
if a==0 and b!=0:
    x1=-c/b
    print("La solution est ",x1)
elif b==0 and a!=0:
    x1=-(c/a)**0.5
    x2=(c/a)**0.5
    print("Les solutions sont ",x1,x2)
elif a==0 and b==0 and c!=0:
    print("Cette equation n'a pas de solution")
elif a==0 and b==0 and c==0:
    print("Il y a une infinite de solutions")
else :
    D=b**2-4*a*c
    x1=(-b-(D**0.5))/2*a
    x2=(-b+(D**0.5))/2*a
    print("Les solutions sont ",x1,x2)

#7.1
k=1
n=int(input("Saisir n "))
for k in range(n+1):
      k=2*k+1
print(k)

#Le reste c'est du n'importe quoi

#8.1

i=1
somme=0
while i<=n:
    somme=somme+i**2
    i=i+1
print("Somme des premiers carres = ",somme)

#8.2
somme2=0
i=1
while i<=n:
    somme2=somme2+i**2
    i=i+2
print("Somme des premiers carres impairs = ",somme2)

#8.3
somme3=0
i=1
while i<=n:
    somme3=somme3+1/(i**2)
    i=i+1
print("Somme des 1/k^2 = ",somme3)
























    
