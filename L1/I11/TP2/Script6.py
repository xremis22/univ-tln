#Script Répétition d'un bloc d'instructions


continu=True

while continu :
    a=int(input("Valeur de a : "))
    b=int(input("Valeur de b : "))
    op=input("Choix d'opérateur parmi (+,-,*,/) : ")
    if op == "+" :
        print("le résultat est",a,"+",b," = ",a+b)
        print("Cette expression est de type",type(a+b))
    elif op == "-" :
        print("le résultat est",a,"-",b," = ",a-b)
        print("Cette expression est de type",type(a-b))
    elif op == "*" :
        print("le résultat est",a,"*",b," = ",a*b)
        print("Cette expression est de type",type(a*b))
    elif op == "/" :
        if b != 0 :
            print("le résultat est",a,"/",b," = ",a/b)
            print("Cette expression est de type",type(a/b))
        else :
            print("On ne peut pas faire une division par 0")
    c=input("Continuer o/n ? ")
    continu=c!="n"
