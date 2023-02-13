#Question 1


def Affiche(c):
	print("X = ", str(c[0]).replace("'",''))
	print("G = ", str(c[1]).replace("'",''))
	print("Y = ", str(c[2]).replace("'",''),end='\n\n')


def Lecture(nomfichier):
	fichier = open(nomfichier,"r")
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
	couple=chaine.rstrip().split("\n",">")

	i=0
	while i < len(liste):
		if chaine[i].isalpha() :
			X.add(chaine[i])
		elif chaine[i].isdigit() :
			Y.add(chaine[i])
		i+=1
	#Triplet (X,G,Y)
	c=(X,G,Y)

	return c



nomfichier=input("Saisisez le nom du fichier : ")
print(Affiche(Lecture(nomfichier)))
