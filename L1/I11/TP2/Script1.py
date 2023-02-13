#Script Gestion des cas 1

note=float(input("Quelle note aviez vouz eu à l'examen ? "))
if note>=10:
	print("Vous avez passé votre examen")
	if note>=16:
		print("Avec mention Très Bien")
	elif note>=16:
		print("Avec mention Bien")
	elif note>=12:
		print("Avec mention Assez Bien")
else:
	print("Vous n'avez pas passé votre examen")
	
