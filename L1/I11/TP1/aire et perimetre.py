#Script2

print("Bienvenu dans la calculatrice pro pour calculer un périmètre et une aire d'un cercle! \n Pour calculer un pérmètre, tapez 1. \n Pour calculer une aire, tapez 2 \n Pour calculer les deux, tapez 3")
pi=3.14159
a=int(input())
if a==1:
    r=int(input("Saisisez la valeur du rayon r \n"))
    print("périmètre du cercle=",pi*r*2)
elif a==2:
    r=int(input("Saisisez la valeur du rayon r \n"))
    print("aire du cercle=",pi*r**2)
else:
    r=int(input("Saisisez la valeur du rayon r \n"))
    print("périmètre du cercle=",pi*r*2);
    print("aire du cercle=",pi*r**2);
