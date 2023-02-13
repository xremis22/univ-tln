import multiprocessing
import random
from egcd import egcd


def print_Mat(A) :
    for i in range(len(A)):
        print(A[i])
    print("\n")

def pgcd(a,b) :
    while (a != b) :
        d = abs(b-a)
        b = a
        a = d
    return d

'''
Question 1
Incomplet
Noté sur 1,00
Texte de la question
Ecrire la fonction gentrianginf_Zm(n,m)
qui renvoie une matrice triangulaire inférieure inversible à n lignes et n colonnes
composée d'éléments de (Z/mZ,+).
Pour que la matrice soit inversible dans (Z/mZ,+),
il faut que le déterminant soit premier avec n.
Attention, cet algorithme s'écrit sans l'instruction if et avec au plus 4 boucles.
Votre fonction sera exécutée dans un environnement où la librairie random a été importé
via l'instruction import random.
'''

def gentrianginf_Zm(n,m) :
    L = []
    for i in range(n) :
        sousL = [0]*n
        for j in range(i+1):
            sousL[j] = random.randrange(0,m)
        L.append(sousL)
        d = 0
        while (d != 1) :
            L[i][i] = random.randrange(0,m)
            d = pgcd(L[i][i], m)
    return L

#print_Mat(gentrianginf_Zm(4, 4))


'''
Question 2
Incomplet
Noté sur 1,00
Non marquéeMarquer la question
Texte de la question
Déduire de la fonction précédente, la fonction genmatrixinv(n,m) qui créée une
matrice n×n inversible dans (Z/mZ,+).
Votre fonction s'exécutera dans un environnement où la fonction transpose(M) est
disponible, ainsi que la fonction gentrianginf_Zm(n,m).
Votre fonction sera exécutée dans un environnement où la librairie random a été
importé via l'instruction import random.
'''

def matmat_mod_m(A,B,m):
    prod = []
    for i in range(len(A)) :
        aux = []
        for j in range(len(B[0])) :
            somme = 0
            for k in range(len(A[0])) :
                somme += (A[i][k] * B[k][j])
            aux += [somme%m]
        prod += [aux]
    return prod

def transpose(M):
    L = []
    for i in range(len(M[0])):
        sousL = []
        for j in range(len(M)):
            sousL.append(M[j][i])
        L.append(sousL)
    return L


def genmatrixinv(n,m) :
    matrixinf = transpose(gentrianginf_Zm(n,m))
    matrixsup = gentrianginf_Zm(n, m)
    resultat = matmat_mod_m(matrixinf, matrixsup, m)
    print_Mat(matrixinf)
    print_Mat(matrixsup)
    return resultat


print_Mat(genmatrixinv(4, 10))

'''
Question 3
Correct
Noté sur 1,00
Non marquéeMarquer la question
Texte de la question
Le système de chiffrement de Hill est un procédé permettant à un
utilisateur A de transmettre de façon confidentielle un message m à un
autre utilisateur B.

Pour cet exercice les messages seront construits à partir de l'alphabet
constitué des symboles  a,b,c,...,z,{,},| .
Cet alphabet étant constitué de 29 symboles, on peut associer un
numéro à chaque symbole : a=0 , b=1 , c=2, ...., z=25, {=26, }=27, | = 28.
L'entier 29 étant un nombre premier, (Z/29Z,+,×) est un corps,
et on peut donc considérer l'espace vectoriel Mn(Z/29Z) des matrices
carrées n×n définies sur le corps fini Z/29Z.

Soit m=(m1,…,mn) un message de taille n, c'est à dire une suite de n
symboles de l'alphabet. Les deux utilisateurs A et B possèdent
tous les deux une même matrice K∈GL(n,Z/29Z), que l'on appelle
communément la clé secrète du système.

Pour envoyer le message m à B, l'utilisateur A calcule le produit du
vecteur m par la matrice K pour obtenir un nouveau vecteur c appelé
cryptogramme. On a donc c=mK. Attention, toutes les opérations sont
effectuées dans le corps Z/29Z.

Exemple : pour n=5, considérons le message "gauss", ce dernier est
représenté par le vecteur m=(6,0,20,18,18). Supposons que la clé K
partagée par A et B soit K=⎛⎝⎜⎜⎜⎜⎜⎜818131422249619471013241593291125552526⎞⎠⎟⎟⎟⎟⎟⎟.
Le cryptogramme  c=mK vaut (28,11,18,19,8) qui correspond à "|ℓsti".
Pour déchiffrer le cryptogramme c, l'utilisateur B calcule cK−1 où
K−1 est l'inverse de la matrice K. La matrice K−1 est obtenue en appliquant
l'algorithme de Gauss dans le corps Z/29Z. Pour l'exemple on a :
K−1=⎛⎝⎜⎜⎜⎜⎜⎜1513723519111711282642172727241289192414205⎞⎠⎟⎟⎟⎟⎟⎟
et le produit cK−1 donne bien (6,0,20,18,18) qui est le message d'origine.
Vous avez intercepté le cryptogramme suivant : (0,7,25,21,11). Ce dernier a
été obtenu en utilisant le protocole de chiffrement de Hill pour
une clé K dont vous ne connaissez pas la valeur.

A l'adresse http://veron.univ-tln.fr/ENSEIGNEMENT/I33/hill.html vous
avez accès à l'interface de chiffrement qui a été utilisée pour produire
ce cryptogramme. Vous pouvez utiliser cette interface pour chiffrer n'importe
quel message de votre choix (sour la forme d'un vecteur de longueur 5
à composantes dans Z/29Z) et obtenir le cryptogramme correspondant.

A partir de cette interface et des fonctions que vous avez précédemment
écrites, pouvez-vous :
donner la valeur de la matrice clé utilisée,
donner la valeur du message qui correspond au cryptogramme (0,7,25,21,11).
Vous rentrerez la valeur de la matrice clé sous la forme d'une liste de
listes et le message sous la forme d'une chaine de caractères.
Exemple :
matrice_cle = [[9,24,7,9,25], [18,9,10,3,5], [13,6,13,2,5], [14,19,24,9,25], [22,4,15,11,26]]
message = "gauss"
'''

'''
[0,0,0,0,1] = (22, 4, 3, 12, 26)
[0,0,0,1,0] = (3, 26, 8, 9, 25)
[0,0,1,0,0] = (13, 7, 1, 2, 5)
[0,1,0,0,0] = (11, 14, 9, 13, 7)
[1,0,0,0,0] = (2, 7, 22, 9, 25)

[1,1,1,1,1] = (22, 0, 14, 16, 1)
'''

D = dict()
D["a"] = 1
D["b"] = 2
D["c"] = 3
D["d"] = 4
D["e"] = 5
D["f"] = 6
D["g"] = 7
D["h"] = 8
D["i"] = 9
D["j"] = 10
D["k"] = 11
D["l"] = 12
D["m"] = 13
D["n"] = 14
D["o"] = 15
D["p"] = 16
D["q"] = 17
D["r"] = 18
D["s"] = 19
D["t"] = 20
D["u"] = 21
D["v"] = 22
D["w"] = 23
D["x"] = 24
D["y"] = 25
D["z"] = 26
D[" "] = 27
D[","] = 28
D["."] = 29

def matvec(M,V):
    L = []
    for i in range(len(M)):
        s = 0
        for j in range(len(V)):
            s += M[i][j]*V[j]
        L.append(s)
    return L

def decrypte_hill(c) :
    decrypt = ""
    L = []

    for lettre in c :
        L.append(D[lettre])


#Chiffrement de Hill :
'''
def decoupe(f_in, n) :
    source = open(f_in, "r")
    L = []
    i = 0
    j = 0
    ligne = ""
    for source in iter(lambda: source.read(n), '') :
        process(source)
        for i in range(len(f_in)) :
            L1 = []
            for j in range(n) :
                L1 += [f_in[i]]
                i += 1
            L += [L1]
    return L


print(decoupe("test.txt", 12))
'''
