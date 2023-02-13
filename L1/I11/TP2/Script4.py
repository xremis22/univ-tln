#Script Equation du second degré
a=float(input("a = "))
b=float(input("b = "))
c=float(input("c = "))
discriminant=float((b**2)-4*a*c)

print("Soit l'équation du second degré y=",a,"x**2","+",b,"x","+",c)

if discriminant>0 :
    if a>0 or a<0 :
        print("Il existe deux solutions dans les réels")
        x1=((-b-(discriminant**0.5))/2*a)
        x2=((-b+(discriminant**0.5))/2*a)
        print(x1)
        print(x2)
    else :
        print("L'equation est du premier degré")
        x=(-c)/b
        print(x)
elif discriminant==0 :
    print("Il existe une solution unique")
    x=((-b)/2*a)
    print(x)
else :
    print("Il n'y a pas de solutions dans les réels")
