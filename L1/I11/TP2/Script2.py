#Script Gestion des cas 2

note1=float(input("Saisisez votre première note d'UE : "))
note2=float(input("Saisisez votre deuxième note d'UE : "))
note3=float(input("Saisisez votre troisième note d'UE : "))
note=(note1 + note2 + note3)/3
if note>=10:
    print("Semestre valide")
    if note1<10 or note2<10 or note3<10:
        print("Par compensation")
else :
    print("Session de rattrapage")
