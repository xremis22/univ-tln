def Int2Bin(entier,n):
	binaire=bin(entier)
	binaire=binaire[2:]
	if len(binaire) < entier:
		calcul=entier-len(binaire)
	return(calcul)
n=int(input("n "))
entier=int(input("entier "))
print(Int2Bin(entier,n))
