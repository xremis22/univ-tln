#Script Equation du second degré1 avec les si

a=float(input("a = "))
b=float(input("b = "))
c=float(input("c = "))
D=(b**2)-(4*a*c)
if a==0:
    if b==0:
        if c==0:
            print("Tout réel est solution")
        else :
            print("Il n'y a pas de solutions")
    else :
        print("C'est une équation du premier degré")
        x=(-c)/b
        print("L'unique solution est x = ",x)
else :
    print("C'est une équation du second degré")
    if D>0 :
        print("Il y a deux solutions dans les réels")
        x1=(-b-(D**(0.5)))/(2*a)
        x2=(-b+(D**(0.5)))/(2*a)
        print("x1 = ",x1)
        print("x2 = ",x2)
    elif D==0 :
        print("Il y a une unique solution")
        x=((-b)/(2*a))
        print("x = ",x)
    else :
        print("Il n'y a pas de solutions dans les réels")
              
