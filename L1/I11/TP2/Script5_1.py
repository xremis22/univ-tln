#Script Calculatrice1
a=int(input("Saisir a : "))
op=input("Saisir le type d'opération : ")
b=int(input("Saisir b : "))

if op == "+" :
    print("a+b = ",a+b)
elif op == "-" :
    print("a-b = ",a-b)
elif op == "*" :
    print("a*b = ",a*b)
elif op == "/" :
    if b != 0 :
        print("a/b = ",a/b)
    else :
        print("On ne peut pas faire une division par 0")
        
