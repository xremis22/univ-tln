fichier = open(correspondance,"r")
liste = fichier.readlines()
print(liste)
#Ensemble de départ est lettres
X=set()
#Ensemble d'arrivée est numéros
Y=set()
#Correspondance est ?
G=()
#On transforme la liste en une chaine pour pouvoir la parcourir avec la commande rstrip
chaine=str(liste)
couple=chaine.rstrip().split(">")
correspondance=correspondance.txt
i=0
while i < len(liste):
  if chaine[i].isalpha() :
    X.add(chaine[i],)
  else :
    Y.add(chaine[i],)
  i+=1
print(X,Y)
