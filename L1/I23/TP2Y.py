#Question 1

def Affiche(c):
	print("X = ", str(c[0]).replace("'",''))
	print("G = ", str(c[1]).replace("'",''))
	print("Y = ", str(c[2]).replace("'",''),end='\n\n')

def Lecture(nomfichier):
	fichier = open(nomfichier,"r")
	liste = fichier.readlines()
	liste1=[]
	i=0
	while i < len(liste):
		liste1+=[liste[i].rstrip().split("\n")]
		i+=1
	X=set()
	Y=set()
	G={}
	for i in liste1 :
		if len(i[0])==3 :
			X=X|set(i[0][0])
			Y=Y|set(i[0][2])
			if not(i[0][0]) in G :
				G[i[0][0]]=set(i[0][2])
			else :
				G[i[0][0]]|=set(i[0][2])
		elif i[0][0].isalpha() :
			X=X|set(i[0][0])
		else :
			Y=Y|set(i[0][1])
	c=(X,G,Y)
	return Affiche(c)
print(Lecture("correspondance.txt"))

#Question 2

def Reciproque(C) :
	
